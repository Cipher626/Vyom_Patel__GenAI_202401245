class Car:

    total_cars=0
    def __init__(self, userbrand, usermodel):

        self.__brand=userbrand
        self.__model=usermodel
        Car.total_cars+=1

    def get_brand(self):
        return self.__brand
    def name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_def():
        return "Car is method of transport"
    
    @property
    def model(self):
        return self.__model
    

    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85KwH")

my_car= Car("Toyota","Corolla")

# print(isinstance(my_tesla,Car))

# print(isinstance(my_tesla,ElectricCar))

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class Electric_Car(Battery,Engine):
    pass

tesla_two=Electric_Car("Tesla","Model4")

print(tesla_two.battery_info())