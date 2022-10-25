import random
from ZSIC import ZeroShotImageClassification
import cv2
from PIL import Image

class ImageClassifier:
    def __init__(self):
        self.model = ZeroShotImageClassification()

    def predict(self, image, candidate_labels=["cats", "dogs"]):
        prediction = self.model(image=image,
            candidate_labels=candidate_labels, 
            )
        return prediction
        # return "cat" if random.random() < 0.5 else "dog"

if __name__ == "__main__":
    image = cv2.imread("demo/dog_demo.jpeg")
    pil_image = Image.fromarray(image)
    model = ImageClassifier()
    print(model.predict(pil_image))