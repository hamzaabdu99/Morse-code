class Cars:

    def __init__(self, car_name, car_model):
        self.car_name = car_name
        self.car_model = car_model

    def car(self):
        return f"A {self.car_model} {self.car_name}"


car1 = Cars("ford", 2020)

print(car1.car())
