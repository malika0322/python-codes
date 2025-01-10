#10. Write a Python program to write a list to a file.
data = ["Hello", "Python", "File Operations"]
with open("list_file.txt", "w") as file:
    for item in data:
        file.write(item + "\n")
print(f"List written to list_file.txt")

#output:List written to list_file.txt