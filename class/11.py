'''11. Create a child class called ElectricCar that inherits from the Car class. Add an attribute 
battery_size to the child class with a default value. Also, add a method describe_battery() 
that prints information about the battery size. '''
#confused
class Car:
    def abc(self, make, model, year):
        self.m = make
        self.mo = model
        self.yr = year

    def describe_car(self):
        print(f"{self.yr} {self.m} {self.mo}")

class ElectricCar(Car):
    def defination(self, make, model, year, battery_size=75):
        self.abc(make, model, year) 
        self.b_size = battery_size

    def describe_battery(self,battery_size):
        self.b_size=battery_size
        print(f"Battery size: {self.b_size} kWh")

# Creating an instance of ElectricCar
electric_car = ElectricCar()

# Displaying battery information
electric_car.describe_battery(75)
electric_car.defination("Tesla", "Model S", 2023)

#output
#Battery size: 75 kWh

