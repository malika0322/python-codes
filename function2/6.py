#6 Write a Python program to access a function inside a function. 
def outer_func():
    def inner_func():
        return "inner function called"
    return inner_func()
print(outer_func)
    