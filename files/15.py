'''15. Ram has used a text editing software to type some text. After saving the article as 
WORDS.TXT, she realized that she has wrongly typed alphabet J in place of alphabet I 
everywhere in the article. Write a function definition for JTOI() in Python that would display 
the corrected version of entire content of the file WORDS.TXT with all the alphabets "J" to be 
displayed as an alphabet "I" on screen. 
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise. '''
with open("WORDS.TXT", "r") as file:
    content = file.read().replace("J", "I")
print(content)

#output:
'''Iolly Iumping Iesters Iuggle Iewels.
Iumping Iacks are fun for everyone.'''
