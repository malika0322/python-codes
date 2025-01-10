#11. Write a Python program to copy the contents of a file to another file. 
with open("poem.txt", "r") as src:
    with open("copy_poem.txt", "w") as dest:
        dest.write(src.read())
print("Content copied to copy_poem.txt")

#output:Content copied to copy_poem.txt