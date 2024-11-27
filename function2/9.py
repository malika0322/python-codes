'''9. Write a Python program to find the power of a number using recursion function. 
Input: N = 2, P = 3 Output: 8 
Input: N = 5, P = 2 Output: 25'''
def power(N,P):
    if P==0:
        return 1
    return N*power(N,P-1)
print(power(2,3))
print(power(5,2))