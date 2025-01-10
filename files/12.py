#12. Write a Python program to read a random line from a file. 
import random

with open("randomfile.txt", "r") as file:
    lines = file.readlines()
print(random.choice(lines).strip())

#output:Line one.
