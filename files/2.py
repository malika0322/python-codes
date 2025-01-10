#2. Write a Python program to read first n lines of a file. 
def read_first_n_lines(file_name, n):
    with open(file_name, "r") as file:
        for i in range(n):
            print(file.readline(), end="")

read_first_n_lines("poem.txt", 2)
#output
'''Twinkle, twinkle, little star,
How I wonder what you are! '''
