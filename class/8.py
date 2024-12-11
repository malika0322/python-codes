'''8. Define a class named Car with attributes make, model, and year. Add a method 
describe_car() that prints a neatly formatted descriptive name of the car. Then, create an 
instance of Car and call this method. '''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

car = Car("Toyota", "Camry", 2021)
car.describe_car()

#output:
# 2021 Toyota Camry