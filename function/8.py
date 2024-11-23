#8. Write a Python function to find the maximum and minimum value, sum and multiplication of all the 
#numbers in a list.
list = [1, 2, 3, 4]
import math
def list_operations(list):
    if not list: 
        return "The list is empty."
    max_value = max(list)
    min_value = min(list)
    total_sum = sum(list)
    product=math.prod(list)
    '''product = 1
    for num in list:
        product *= num'''
    return {
        "Maximum": max_value,
        "Minimum": min_value,
        "Sum": total_sum,
        "Product": product
    }
result = list_operations(list)
print(result)


