import pika, sys, os
import cv2
import json
import base64
import numpy as np
from utils import decode_jpg_from_string

from models.ocr import OCR
from database import replace_dataset_by_id, find_dataset_by_id

# initial ocr model
model = OCR()

def main():
    """
    receive image from ocr queue and recognize it
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="ocr")

    async def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body)["file_name"])
        image = decode_jpg_from_string(json.loads(body)["image"])
        print("prediction result:", model.predict(image))
        # dataset = await find_dataset_by_id(json.loads(body)["dataset_id"])
        # print(dataset)

        # cv2.imshow("image", image)
        # cv2.waitKey(0) 
    
    channel.basic_consume(queue="ocr", on_message_callback=, auto_ack=True)
    
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
