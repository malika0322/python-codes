#5 Write a Python function to create and print a list where the values are the squares of numbers between 
#1 and 20 (both included). 
def square_list():
    squares=[]
    for i in range(1,21):
        squares.append(i**2)
    return squares
print(square_list())