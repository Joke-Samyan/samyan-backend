import pika
import cv2
import json
import base64
from utils import encode_jpg_from_path


def send_to_image_classifier_queue(image_path="./demo/dog_demo.jpeg", file_name="dog_demo.jpeg"):
    """
    Send an image to the image classifier queue
    """
    encoded_image = encode_jpg_from_path(image_path)
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
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

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="ocr")

    # send json with file name and encoded image
    channel.basic_publish(exchange="",
                          routing_key="ocr",
                          body=json.dumps({"image": encoded_image,
                                           "file_name": file_name}))

    print(" [x] Sent image to ocr queue")

    connection.close()


def main():
    send_to_image_classifier_queue()
    send_to_ocr_queue()


if __name__ == "__main__":
    main()