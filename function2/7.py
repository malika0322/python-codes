#7 Write a Python program to detect the number of local variables declared in a function. 
def func():
    a=2
    b=3
    c=4
print(func.__code__.co_nlocals)