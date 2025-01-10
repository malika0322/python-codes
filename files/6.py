#6. Write a Python program to read a file line by line store it into a variable. 
with open("poem.txt", "r") as file:
    content = file.read()
print(content)

#output:
'''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
And I like Python!'''