#3. Write a Python program to count the number of lines in a text file which starts with an alphabet “T”.
count = 0
with open("notes.txt", "r") as file:
    for line in file:
        if line.startswith("T"):
            count += 1
print(f"Lines starting with 'T': {count}")

#output:Lines starting with 'T': 3