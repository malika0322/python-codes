#8. Write a Python program to count and display the total number of words in a file.
with open("poem.txt", "r") as file:
    words = file.read().split()
print(f"Total words: {len(words)}")

#output:Total words: 26