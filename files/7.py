#7. Write a Python program to read a file line by line store it into an array.
with open("poem.txt", "r") as file:
    lines = [line for line in file]
print(lines)

#output:
'''['Twinkle, twinkle, little star,\n', 'How I wonder what you are!\n',
 'Up above the world so high,\n', 'Like a diamond in the sky.\n', 'And I like Python!\n']'''