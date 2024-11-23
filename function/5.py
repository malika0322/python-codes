#5. Modify above function so that it has default values of 2 for both length and width. 
#a=int(input("enter length"))
#b=int(input("enter width"))
#c=input("a or p")
a,b=2,2
def rectange(a,b):
    area=a*b
    perimeter=2*(a+b)
    return area,perimeter
    # return perimeter  
ar,p=rectange(a,b)
print(ar)
print(p)