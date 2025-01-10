#13. Write a Python program to remove newline characters from a file. 
with open("poem.txt", "r") as file:
    content = file.read().replace("\n", "")
print(content)

#outout:
'''Twinkle, twinkle, little star,How I wonder what you are!
Up above the world so high,Like a diamond in the sky.And I like Python!'''