'''14. Override the describe_car() method in the ElectricCar class to include information about 
its battery size along with the car's make, model, and year. '''

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

    def describe_car(self):
        print(f"make:{self.m} model:{self.mo} year:{self.yr} Battery size: {self.b_size} kWh")
electric_car = ElectricCar("Tesla", "Model S", 2023)

# Displaying battery information
electric_car.describe_car()

#output
# make:Tesla model:Model S year:2023 Battery size: 75 kWh



