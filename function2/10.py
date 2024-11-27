#10. Write a Python function that takes a sentence as a parameter and print the words in ascending order.
def asce(sentence):
    words=sentence.split()
    return " ".join(sorted(words))
print(asce("hi this is malika"))