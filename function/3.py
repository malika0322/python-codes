#3. Write a Python function to calculate the factorial of a number (a non-negative integer) with and without 
#using recursion. The function accepts the number as an argument.  
# without recursion
n=int(input ("enter the value of n"))
def fact(n) :
    result=1
    for i in range (1, n+1) :
        result*=i
    return result
result=fact (n)
print("fact=",result)
# with
n=int(input("enter the value of n"))
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
result=fact(n)
print("fact:",result)