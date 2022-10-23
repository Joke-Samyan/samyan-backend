import json
from fastapi import APIRouter
import requests
from dotenv import load_dotenv
import os
from src.schema import DatasetSchema, AnnotateSchema

load_dotenv(".env")
REST_URL = os.environ.get("REST_URL")

rest_router = APIRouter(
    prefix="/REST", tags=["REST"], responses={404: {"description": "Not Found"}}
)

@rest_router.get("/test")
def test():
    r = requests.get(REST_URL+"/")
    return r.json()

@rest_router.get("/dataset")
def dump_dataset():
    r = requests.get(REST_URL+"/dataset")
    return r.json()

@rest_router.post("/dataset/create")
def create_dataset(request: DatasetSchema):
    data = request.__dict__
    for idx, entry in enumerate(data["entries"]):
        data["entries"][idx] = entry.__dict__
    r = requests.post(REST_URL+"/dataset/create", json = data)
    return r.json()

@rest_router.put("/annotate")
def annotate(request: AnnotateSchema):
    data = request.__dict__
    r = requests.put(REST_URL+"/annotate", json=data)
    return r.json()


