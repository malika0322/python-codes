'''13. Add a new method to the ElectricCar class that calculates the range of the car based on the 
battery size. The method should print a message indicating the range.'''

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

    def calculate_range(self):
        range = self.b_size * 3
        print(f"This car can go approximately {range} miles on a full charge.")


my_electric_car = ElectricCar("Tesla", "Model S", 2024, battery_size=100)
my_electric_car.describe_car()
my_electric_car.calculate_range()

#output:
# make:Tesla model:Model S year:2024 Battery size: 100 kWh
# This car can go approximately 300 miles on a full charge.