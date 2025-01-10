# 1. Write a function in python to read the content from a text file "poem.txt" line by line and 
# display the same on screen  
def read_file_line_by_line():
    with open("poem.txt", "r") as file:
        for line in file:
            print(line, end="")
read_file_line_by_line()
#output
'''Twinkle, twinkle, little star,
How I wonder what you are! 
Up above the world so high,
Like a diamond in the sky. '''