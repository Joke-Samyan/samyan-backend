import random

class OCR:
    def __init__(self):
        pass

    def predict(self, image):
        return "meow" if random.random() < 0.5 else "bark"