import pika, sys, os
import cv2
import json
import base64
import numpy as np

from models.ocr import OCR

# initial ocr model
model = OCR()

def main():
    """
    receive image from ocr queue and recognize it
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="ocr")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body)["file_name"])
        jpg_original = base64.b64decode(json.loads(body)["image"])
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        image = cv2.imdecode(jpg_as_np, flags=1)
        print("prediction result:", model.predict(image))

        # cv2.imshow("image", image)
        # cv2.waitKey(0) 
    
    channel.basic_consume(queue="ocr", on_message_callback=callback, auto_ack=True)
    
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
