'''11. Write a Python a function that takes a string as argument and print the most common character in that 
string. '''
def most_common_char(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    max_char= None
    max_count=0
    for char, count in freq.items():
        if count> max_count:
            max_count=count
            max_char=char
    return max_char
print(most_common_char("proggramming"))