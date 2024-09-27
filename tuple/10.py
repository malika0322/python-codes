'''10. Write a Python program to compute the element-wise sum of given tuples. 
Original lists: 
 (1, 2, 3, 4)
(3, 5, 2, 1) 
(2, 2, 3, 1) 
Element-wise sum of the said tuples: 
(6, 9, 8, 6) '''
t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)
element_wise_sum = tuple(a + b + c for a, b, c in zip(t1, t2, t3))
print("Element-wise sum of the said tuples:")
print(element_wise_sum)