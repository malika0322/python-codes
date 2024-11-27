#4 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
newlist=[]
def list(original_list):
    for i in original_list:
        newlist.append(i*2)
original_list = [1, 2, 3]
list(original_list)
print(newlist)