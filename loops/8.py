'''8. Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2''' 
s=input("enter a string")
digits=letters=0
for i in s:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
print(f"digits,{digits}")
print(f"letters,{letters}")

