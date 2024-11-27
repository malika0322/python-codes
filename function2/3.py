#3 Write a Python function that accepts a string and counts the number of vowel and consonant letters. 
def vandc(s):
    v="aeiou"
    vowel=0
    consonant=0
    for char in s:
        if char.isalpha():
            if char in v:
                vowel+=1
            else:
                consonant+=1
    return vowel,consonant
print(vandc("hellomalika"))

