import random

class ImageClassifier:
    def __init__(self):
        pass

    def predict(self, image):
        return "cat" if random.random() < 0.5 else "dog"
        