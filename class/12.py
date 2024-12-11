'''12. Modify the ElectricCar class to include an __init__() method that properly initializes the 
parent class's attributes as well as its own attribute battery_size. '''
class Car:
    def __init__(self, make, model, year):
        self.m = make
        self.mo = model
        self.yr = year

    def describe_car(self):
        print(f"{self.yr} {self.m} {self.mo}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year) 
        self.b_size = battery_size

    def describe_battery(self):
        print(f"Battery size: {self.b_size} kWh")

# Creating an instance of ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 2023)

# Displaying battery information
electric_car.describe_battery()

#output
# Battery size: 75 kWh

