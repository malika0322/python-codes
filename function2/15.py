#15. Write a Python function takes a two-word strings and find if both words begin with same 
# letter or not.
def same_start_letter(two_word_string):
    words = two_word_string.split()
    if len(words) != 2:
        return "Input must be a two-word string."
    return words[0][0].lower() == words[1][0].lower()
print(same_start_letter("Happy Hummingbird")) 
print(same_start_letter("Happy Bird"))         
print(same_start_letter("One"))    
            
