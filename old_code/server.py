from typing import Union, List
from pymongo import MongoClient
from fastapi import FastAPI, Body, Request, Response, HTTPException, status
from database import insert_dataset, find_dataset_by_id
from schema import DatasetSchema, AnnotateSchema, CreateUserSchema
import bson

app = FastAPI()
MONGO_DETAILS = "mongodb://localhost:27017"

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGO_DETAILS)
    app.database = app.mongodb_client["kodwang"]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/dataset/")
def get_all_datasets(request:Request):
    datasets = [e for e in request.app.database.dataset.find({})]
    for dataset in datasets:
        dataset_id = str(dataset.pop("_id"))
        dataset["dataset_id"] = dataset_id
        for entry in dataset["entries"]:
            entry_id = entry.pop("entry_id")
            entry["entry_id"] = str(entry_id)
    return datasets

@app.get("/dataset/{id}")
def get_dataset_by_id(id:str, request:Request):
    dataset = request.app.database.dataset.find_one({"_id": bson.ObjectId(id)})
    dataset["dataset_id"] = str(dataset.pop("_id"))
    for entry in dataset["entries"]:
        entry["entry_id"] = str(entry.pop("entry_id"))
    if dataset is not None:
        return dataset
    return False

@app.post("/dataset")
def add_dataset(dataset_data: DatasetSchema, request: Request):
    dataset_data = dataset_data.__dict__
    dataset_data["entries"] = [e.__dict__ for e in dataset_data["entries"]]
    for idx, entry in enumerate(dataset_data["entries"]):
        temp = entry
        temp["entry_id"] = bson.ObjectId()
        dataset_data["entries"][idx] = temp
    try:
        request.app.database.dataset.insert_one(dataset_data)
        return {"ok": 1, "id": str(dataset_data["_id"])}
    except Exception as e:
        print(e)
        return {"ok": 0}

@app.put("/annotate")
def add_annotate(annotate: AnnotateSchema, request:Request):
    dataset = request.app.database.dataset.find_one({"_id": bson.ObjectId(annotate.dataset_id)})
    request.app.database.dataset.delete_one({"_id": bson.ObjectId(annotate.dataset_id)})
    for idx, entry in enumerate(dataset["entries"]):
        if entry["entry_id"] == bson.ObjectId(annotate.entry_id):
            temp = entry
            temp["label"] = annotate.label
            temp["labeler_id"] = annotate.labeler_id
            dataset["entries"][idx] = temp
            break
    request.app.database.dataset.insert_one(dataset)
    current_balance = request.app.database.user.find_one({"_id": bson.ObjectId(annotate.labeler_id)})["balance"]
    request.app.database.user.update_one({"_id": bson.ObjectId(annotate.labeler_id)}, { "$set": { "balance": current_balance+temp["reward"] } })
    
    dataset = request.app.database.dataset.find_one({"_id": bson.ObjectId(annotate.dataset_id)})
    dataset["dataset_id"] = str(dataset.pop("_id"))
    for entry in dataset["entries"]:
        entry["entry_id"] = str(entry.pop("entry_id"))
    if dataset is not None:
        return dataset

@app.delete("/dataset")
def delete_all_dataset(request: Request):
    try:
        request.app.database.dataset.delete_many({})
        return {"ok": 1}
    except Exception:
        return {"ok": 0}

@app.post("/user")
def create_user(create_user: CreateUserSchema, request:Request):
    create_user = create_user.__dict__
    create_user["balance"] = 0
    create_user["password"] = f"hash_later_kub({create_user['password']})"
    request.app.database.user.insert_one(create_user)
    create_user["user_id"] = str(create_user.pop("_id"))
    print(create_user)
    return create_user

@app.get("/user/{id}")
def get_user(id:str, request:Request):
    user = request.app.database.user.find_one({"_id": bson.ObjectId(id)})
    user["user_id"] = str(user.pop("_id"))
    return user