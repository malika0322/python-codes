#4. Write a python function that takes two parameters length and width and returns the area and perimeter 
#of a rectangle.
a=int(input("enter length"))
b=int(input("enter width"))
#c=input("a or p")
def rectange(a,b):
    area=a*b
    perimeter=2*(a+b)
    return area,perimeter
    # return perimeter  
ar,p=rectange(a,b)
print(ar)
print(p)
