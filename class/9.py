'''9. Modify the Car class so that it has a default value for an attribute called fuel_level, with a 
default value of 100. Add a method check_fuel_level() that prints the car's current fuel level.'''
class Car:
    def __init__(self, make, model, year, fuel_level=100):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def check_fuel_level(self):
        print(f"Fuel level: {self.fuel_level}")

car = Car("Toyota", "Camry", 2021,200)
car.check_fuel_level()

#output:
#Fuel level: 200
