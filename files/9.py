# 9. Write a function in Python to read lines from a text file "notes.txt". Your function should find 
# and display the occurrence of the word "the". 
with open("notes.txt", "r") as file:
    content = file.read().lower()
print(f"Occurrences of 'the': {content.count('the')}")

#output:Occurrences of 'the': 5