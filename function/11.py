#11. Write a function that takes a list of numbers and print each number doubled. 
newlist=[]
def list(original_list):
    for i in original_list:
        newlist.append(i*2)
original_list = [1, 2, 3]
list(original_list)
print(newlist)


