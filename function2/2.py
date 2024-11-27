#2. Write a Python function to check whether a number falls within a given range. 
n=int(input("enter number"))
def in_range(num,start,end):
    return start<=num<=end
print(in_range(n,1,6))