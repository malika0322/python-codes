#7. Write a function that takes two arguments, name and age and returns a dictionary with these as keys and 
#their respective values. 
name=input("enter name")
age=int(input("enter age"))
def func(name,age):
    return {"name":name,"age":age}
a=func(name,age)
print(a)