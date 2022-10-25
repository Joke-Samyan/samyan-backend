import json
from fastapi import APIRouter
import requests
from dotenv import load_dotenv
import os
from src.schema import PrelabelImageSchema
import pika
import cv2
import base64
import numpy as np
import urllib

load_dotenv(".env")
MQ_URL = os.environ.get("MQ_URL")

def decode_jpg_from_string(encoded_string):  
    jpg_original = base64.b64decode(encoded_string)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    image = cv2.imdecode(jpg_as_np, flags=1)
    return image

def encode_jpg_from_path(image_path):
    image = cv2.imread(image_path)
    encoded_image = base64.b64encode(cv2.imencode(".jpg", image)[1]).decode()
    return encoded_image

def encode_jpg_from_array(image):
    encoded_image = base64.b64encode(cv2.imencode(".jpg", image)[1]).decode()
    return encoded_image

def read_img_from_url(url):
    url_response = urllib.request.urlopen(url)
    image = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)
    return image

def send_to_image_classifier_queue(url, dataset_id, entry_id, file_name="dog_demo.jpeg"):
    """
    Send an image to the image classifier queue
    """
    image = read_img_from_url(url)
    encoded_image = encode_jpg_from_array(image)
    # encoded_image = encode_jpg_from_path(image_path)
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="image_classifier")

    # send json with file name and encoded image
    channel.basic_publish(exchange="",
                          routing_key="image_classifier",
                          body=json.dumps({"image": encoded_image,
                                           "file_name": file_name,
                                           "dataset_id": dataset_id,
                                           "entry_id": entry_id
                                           }))

    print(" [x] Sent image to image_classifier queue")

    connection.close()

def send_to_ocr_queue(url, dataset_id, entry_id, file_name="dog_demo.jpeg"):
    """
    Send an image to the ocr queue
    """
    image = read_img_from_url(url)
    encoded_image = encode_jpg_from_array(image)
    # encoded_image = encode_jpg_from_path(image_path)
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="ocr")

    # send json with file name and encoded image
    channel.basic_publish(exchange="",
                          routing_key="ocr",
                          body=json.dumps({"image": encoded_image,
                                            "file_name": file_name,
                                           "dataset_id": dataset_id,
                                           "entry_id": entry_id
                                           }))


    print(" [x] Sent image to ocr queue")

    connection.close()

mq_router = APIRouter(
    prefix="/mq", tags=["mq"], responses={404: {"description": "Not Found"}}
)

@mq_router.post("/image_classifier/")
def prelabel_image_classifier(request: PrelabelImageSchema):
    request = request.__dict__
    try:
        send_to_image_classifier_queue(url=request["url"], file_name="HELLO.jpeg")
    except Exception as e:
        print(e)
        return {"ok": 0}
    return {"ok": 1}


@mq_router.post("/ocr/")
def prelabel_ocr(request: PrelabelImageSchema):
    request = request.__dict__
    try:
        send_to_ocr_queue(url=request["url"], file_name="HELLO.jpeg")
    except Exception as e:
        print(e)
        return {"ok": 0}
    return {"ok": 1}

