#14. Write a Python function that takes a sentence, and return a sentence with the words reversed.
def asce(sentence):
    words=sentence.split()
    return " ".join(sentence.split()[::-1])
print(asce("hi this is malika"))