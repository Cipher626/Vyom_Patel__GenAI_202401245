class Car:
    def __init__(self, userbrand, usermodel):

        self.brand=userbrand
        self.model=usermodel

    def name(self):
        return f"{self.brand} {self.model}"

my_car= Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.name())