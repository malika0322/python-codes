'''10. Add a method to the Car class that allows you to update the car's fuel_level. Then, create an 
instance of Car, update its fuel_level to 50, and call check_fuel_level() to verify the change. '''
class Car:
    def __init__(self, make, model, year, fuel_level=100):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def check_fuel_level(self):
        print(f"Fuel level: {self.fuel_level}")

    def update_fuel_level(self, fuel_level_u):
        self.fuel_level = fuel_level_u

# Creating an instance of the Car class
car = Car("Toyota", "Camry", 2021)

# Updating the fuel level to 50
car.update_fuel_level(50)

# Verifying the updated fuel level
car.check_fuel_level()

#output:
#Fuel level: 50

