class Car:
    make = "hyundai"
    model = "i10"

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print(self):
        msg = "This car is " + self.make + " " + self.model
        print(msg)

