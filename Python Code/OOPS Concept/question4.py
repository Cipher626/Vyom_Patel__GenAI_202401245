class Car:
    def __init__(self, userbrand, usermodel):

        self.__brand=userbrand
        self.model=usermodel

    def get_brand(self):
        return self.__brand
    def name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

# my_tesla = ElectricCar("Tesla", "Model S", "85KwH")

# print(my_tesla.name())

my_car= Car("Toyota","Corolla")
# print(my_car.brand)
print(my_car.get_brand())