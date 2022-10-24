import json
from fastapi import APIRouter
import requests
from dotenv import load_dotenv
import os
import pika
import cv2
import base64

load_dotenv(".env")
MQ_URL = os.environ.get("MQ_URL")

def send_to_image_classifier_queue(image_path="./demo/dog_demo.jpeg", file_name="dog_demo.jpeg"):
    """
    Send an image to the image classifier queue
    """
    image = cv2.imread(image_path)
    encoded_image = base64.b64encode(cv2.imencode(".jpg", image)[1]).decode()

    connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue="image_classifier")

    # send json with file name and encoded image
    channel.basic_publish(exchange="",
                          routing_key="image_classifier",
                          body=json.dumps({"image": encoded_image,
                                           "file_name": file_name}))

    print(" [x] Sent image to image_classifier queue")

    connection.close()

def send_to_ocr_queue(image_path="./demo/dog_demo.jpeg", file_name="dog_demo.jpeg"):
    """
    Send an image to the ocr queue
    """
    image = cv2.imread(image_path)
    encoded_image = base64.b64encode(cv2.imencode(".jpg", image)[1]).decode()

    connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue="ocr")

    # send json with file name and encoded image
    channel.basic_publish(exchange="",
                          routing_key="ocr",
                          body=json.dumps({"image": encoded_image,
                                           "file_name": file_name}))

    print(" [x] Sent image to ocr queue")

    connection.close()


mq_router = APIRouter(
    prefix="/mq", tags=["mq"], responses={404: {"description": "Not Found"}}
)

@mq_router.get("/image_classifier")
def prelabel_image_classifier():
    try:
        send_to_image_classifier_queue(image_path="/Users/napatcheetanom/Desktop/kodwang/prelabel/demo/dog_demo.jpeg", file_name="HELLO.jpeg")
    except Exception:
        return {"ok": 0}
    return {"ok": 1}


@mq_router.get("/ocr")
def prelabel_ocr():
    try:
        send_to_ocr_queue(image_path="/Users/napatcheetanom/Desktop/kodwang/prelabel/demo/dog_demo.jpeg", file_name="HELLO.jpeg")
    except Exception:
        return {"ok": 0}
    return {"ok": 1}

