'''13. Write a Python function that takes a name (string) as argument and capitalizes the first 
and fourth letters of the input name. '''
def capitalize_first_and_fourth(name):
    if len(name) < 4: 
        return "Input must be at least 4 characters long."
    result = name[:1].upper() + name[1:3] + name[3:4].upper() + name[4:]
    return result

print(capitalize_first_and_fourth("alexander")) 
print(capitalize_first_and_fourth("john"))      
print(capitalize_first_and_fourth("max"))     
