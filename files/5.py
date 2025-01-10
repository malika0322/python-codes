#5. Write a Python program to read a file line by line and store it into a list.
with open("poem.txt",'r') as f:
    print(f.readlines()) 