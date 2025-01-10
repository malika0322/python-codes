#4. Write a Python program to append text to a file and display the text.
text_to_append = "And I like Python!"
with open("poem.txt", "a") as file:
    file.write(text_to_append + "\n")

with open("poem.txt", "r") as file:
    print(file.read())

#output:
'''Twinkle, twinkle, little star,
How I wonder what you are!    
Up above the world so high,   
Like a diamond in the sky.    
And I like Python!'''