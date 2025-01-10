#14. Write a Python program to extract characters from various text files and puts them into a list.
with open("poem.txt", "r") as file:
    chars = list(file.read())
print(chars)

#output:
'''['T', 'w', 'i', 'n', 'k', 'l', 'e', ',', ' ', 't', 'w', 'i', 'n', 'k', 'l', 'e',
 ',', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 's', 't', 'a', 'r', ',', '\n', 
 'H', 'o', 'w', ' ', 'I', ' ', 'w', 'o', 'n', 'd', 'e', 'r', ' ', 'w', 'h', 'a', 't',
   ' ', 'y', 'o', 'u', ' ', 'a', 'r', 'e', '!', '\n', 'U', 
'p', ' ', 'a', 'b', 'o', 'v', 'e', ' ', 't', 'h', 'e', ' ', 
'w', 'o', 'r', 'l', 'd', ' ', 's', 'o', ' ', 'h', 'i', 'g', 'h', ',', '\n', 
'L', 'i', 'k', 'e', ' ', 'a', ' ', 'd', 'i', 'a', 'm', 'o', 'n', 'd', ' ',
 'i', 'n', ' ', 't', 'h', 'e', ' ', 's', 'k', 'y', '.', '\n', 
 'A', 'n', 'd', ' ', 'I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!', '\n']'''