# 6. Write a python function that accepts radius and returns the area and circumference of a circle. Import 
# Pi from Math. 
import math
radius=1
def circle(radius):
    area=math.pi*radius*radius
    circumference=2*math.pi*radius
    return area,circumference
    # return perimeter  
ar,c=circle(radius)
print(ar)
print(c)