'''6. Write a Python class named Dog that has two attributes: name and age. Then, create an 
instance of your Dog class and print out the name and age of the dog. '''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Max", 4)
print(f"Name: {dog.name}, Age: {dog.age}")

#output:
# Name: Max, Age: 4