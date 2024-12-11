'''7. Create two instances from the Dog class. For the first instance, set the name to 'Bruno' and 
age to 2. For the second instance, set the name to 'Sher' and age to 3. Print out the information 
for both dogs. '''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating two instances of the Dog class
dog1 = Dog("Bruno", 2)
dog2 = Dog("Sher", 3)
# print(vars(dog1))
# Printing the information for both dogs
print(f"Dog 1 - Name: {dog1.name}, Age: {dog1.age}")
print(f"Dog 2 - Name: {dog2.name}, Age: {dog2.age}")

#output
# Dog 1 - Name: Bruno, Age: 2
# Dog 2 - Name: Sher, Age: 3

