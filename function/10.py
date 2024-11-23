'''10. Create a function that takes a list and a number, return a list after adding the number to the list preventing 
it from changing the original list.'''
def add_to_list(original_list, number):
    new_list = original_list[:]
    new_list.append(number)
    return new_list
original_list = [1, 2, 3]
number = 4
result = add_to_list(original_list, number)
print("Original list:", original_list) 
print("New list:", result)            
