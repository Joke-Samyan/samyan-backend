import random
from ZSIC import ZeroShotImageClassification
import cv2
class ImageClassifier:
    def __init__(self):
        self.model = ZeroShotImageClassification()

    def predict(self, image_path, candidate_labels=["cats", "dogs"]):
        prediction = self.model(image=image_path,
            candidate_labels=candidate_labels, 
            )
        return prediction
        # return "cat" if random.random() < 0.5 else "dog"

if __name__ == "__main__":
    # image = cv2.imread("demo/dog_demo.jpeg")
    model = ImageClassifier()
    print(model.predict("demo/dog_demo.jpeg"))