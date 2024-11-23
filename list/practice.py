#1. Write a Python Program to print all the items in a list. 
# my_list=[1,2,3,4,5]
# for i in my_list:
#     print(i,end=" ")

#2. Use range function to print all the even numbers from 1 to 10. 
# for i in range(2,11,2):
#     print(i)

#3. Write a Python Program to get the largest and smallest number in a list without using built
#in functions. 
# my_list=[1,4,6,7,8,2]
# smallest=my_list[0]
# largest=my_list[0]
# for num in my_list:
#     if num<smallest:
#         smallest=num
#     elif num>largest:
#         largest=num
# print(smallest)
# print(largest)

#4. Write a Python program to find the second smallest and second largest numbers in a list.
# my_list=[1,4,6,7,8,2]
# my_list.sort()
# print(my_list[1])
# print(my_list[-2])

#5. Write a Python program to sum all the items in a list. 
# my_list=[1,4,6,7,8,2]
# sum=0
# for i in my_list:
#     sum+=i
# print(sum)

#6. Write a Python program to multiply all the items in a list.
# my_list=[1,2]
# sum=1
# for i in my_list:
#     sum*=i
# print(sum)

#7. Write a Python program to check if a list is empty or not. 
# my_list=[1,2]
# if not my_list:
#     print("empty")
# else:
#     print("not empty")

#8. Write a Python program to print the numbers of a specified list after removing even 
#numbers from it.
# my_list=[1,4,6,7,8,2]
# newlist=[]
# for i in my_list:
#     if i%2!=0:
#         newlist.append(i)
# print(newlist)

# 9. Write a Python Program to print a specified list after removing the 0th, 4th and 5th element. 
#Sample_list=['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output: [‘Green’, ‘White’, ‘Black’]

# new=[Sample_list[i] for i in range(len(Sample_list)) if i not in [0,4,5]]
# print(new)

#4. Write a Python program to replace the last value of tuples in a list. 
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
# list=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# news=[]
# for i in list:
#     new=i[:-1]+(100,)
#     news.append(new)
# print(news)

#5. Write a Python program to sort a tuple by its float element. 
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')] 
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
# # Sample data
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
float_values = []
for i in range(len(data)):
    float_values.append((float(data[i][1]), i))
float_values.sort(reverse=True)


sorted_data = []
for i in float_values:
     sorted_data.append(data[i[1]])

print(sorted_data)
'''8. Write a Python program to calculate the average value of the numbers in a given tuple of 
# tuples. '''
data=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
for tup in data:
    total_sum = 0
    count = 0
    for num in tup:
        total_sum += num
        count += 1
    average = total_sum / count
    print(average,end=" ,")

    '''1. Write a Python program to create a python dictionary with the following key-value pairs: 
'name':'Hari', 'age':'29, 'city':'Bhaktapur'. Then print the value associated with the key 'age'. '''
 
person = {'name': 'Hari', 'age': '29', 'city': 'Bhaktapur'}
# print(person['age'])

# person['roll']='10a'
# print(person)
# person['city']='kathmandu'
# print(person)
# person.pop('age',None)
# print(person)
# for key,value in person.items():
#     print(f"{key}:{value}")

# Write a Python program to sort a dictionary by its keys.
# dict1={1:"malika",3:'a',2:"b"}
# new=dict(sorted(dict1.items()))
# print(new)



# Input dictionary
# data = {'a': 3, 'b': 1, 'c': 2, 'd': 4}

# # Sort the dictionary by values
# sorted_dict = {}
# for value in sorted(data.values()):
#     for key in data:
#         if data[key] == value :
#             sorted_dict[key] = value
#             break

# # Output the sorted dictionary
# print("Dictionary sorted by values:", sorted_dict)

'''Write a Python program to sort a list alphabetically in a dictionary. 
Sample: num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
Output: {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]} '''
# num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for key,value in num_dict.items():
#     num_dict[key]=sorted(value)
# print(num_dict)

'''Given a dictionary d = {'a':1, b':2, 'c':3}, write a python script to reverse the key-value pairs to 
get a new dictionary. '''
# d ={'a':1,'b':2,'c':3}
# # new={value:key for key,value in d.items()}
# new={}
# for key,value in d.items():
#     new[value]=key
# print(new)
'''Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string : 'engineerings' 
Expected output: 'e': 3, 'n': 2, 'g': 2, 'i': 2, 'r': 1, 's': 1} '''
# # Input string
# string = 'engineerings'

# # Initialize an empty dictionary to store counts
# l = {}

# # Iterate through each character in the string
# for char in string:
#     if char in l:
#         l[char] += 1  # Increment the count if the character is already in the dictionary
#     else:
#         l[char] = 1  # Initialize the count for new characters

# # Output the resulting dictionary
# print("Character frequency dictionary:", l)

#Write a Python program to find the highest 3 values of corresponding keys in a dictionary. 
z={'e': 3, 'n': 2, 'g': 2, 'i': 2, 'r': 1, 's': 1}
new=sorted(z.values(),reverse=True)[:3]
print(new)














