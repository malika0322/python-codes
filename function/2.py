#2. Write a Python function to find the maximum of three input numbers.
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def find_max():
    if a>b and a>c:
        print("a is maximum")
    elif b>c:
        print("b is max")
    else:
        print("c is max")
find_max()
    


