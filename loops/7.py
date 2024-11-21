'''7. Write a Python program to input n numbers from user; count the number of even and odd numbers
from the input numbers and exit until the user input ‘0''''
even_count=0
odd_count=0
num=int(input("enter numbers"))
while num!=0:
       if num%2==0:
             even_count+=1
       else:
             odd_count+=1
       num=int(input("enter numbers"))
print("no of even numbers",even_count)
print("no of even numbers",odd_count)
