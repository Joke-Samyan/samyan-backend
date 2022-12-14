import json
from fastapi import APIRouter, Depends
import requests
from dotenv import load_dotenv
import os
from src.schema import DatasetSchema, AnnotateSchema
from src.utils import validate_token
from src.routers.rabbitmq_router import send_to_image_classifier_queue, send_to_ocr_queue

load_dotenv(".env")
REST_URL = os.environ.get("REST_URL")

rest_router = APIRouter(
    prefix="/REST", tags=["REST"], responses={404: {"description": "Not Found"}}
)

@rest_router.get("/test")
def test(user = Depends(validate_token)):
    r = requests.get(REST_URL+"/")
    return r.json()

@rest_router.get("/dataset")
def dump_dataset(user = Depends(validate_token)):
    r = requests.get(REST_URL+"/dataset")
    return r.json()

@rest_router.post("/dataset/create")
def create_dataset(request: DatasetSchema, user = Depends(validate_token)):
    request = request.__dict__
    request["owner"] = user["user_id"]
    for idx, entry in enumerate(request["entries"]):
        request["entries"][idx] = entry.__dict__
    prelabel = request.pop("prelabel")
    r = requests.post(REST_URL+"/dataset/create", json = request)
    data = r.json()
    entries = data["entries"]

    if prelabel == "IC":
        for e in entries:
            entry = e["entry"]
            entry_id = e["entry_id"]
            entry_type = e["entry_type"]
            if entry_type == "image":
                send_to_image_classifier_queue(entry, data["dataset_id"], entry_id)

    if prelabel == "OCR":
        for e in entries:
            entry = e["entry"]
            entry_id = e["entry_id"]
            entry_type = e["entry_type"]
            if entry_type == "image":
                send_to_ocr_queue(entry, data["dataset_id"], entry_id)


    return r.json()

@rest_router.put("/annotate")
def annotate(request: AnnotateSchema, user = Depends(validate_token)):
    data = request.__dict__
    data["labeler_id"] = user["user_id"]
    r = requests.put(REST_URL+"/annotate", json=data)
    return r.json()


