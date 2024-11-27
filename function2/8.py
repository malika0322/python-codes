'''8. Write a Python program to count the even and odd numbers from a given list and also print them 
separately.'''
def count(lst):
    even=[]
    odd=[]
    for num in lst:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    return len(even),even,len(odd),odd
print(count([1,2,3,4,5,6]))