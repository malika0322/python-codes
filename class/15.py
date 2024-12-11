'''15. Assume you have another file called car.py that contains the Car class. Write a new Python 
script that imports the Car class from car.py, creates an instance of Car, and calls the 
describe_car() method.'''

from car import Car  
my_car = Car("Toyota", "Corolla", 2021)

my_car.describe_car()

#output
# 2021 Toyota Corolla
