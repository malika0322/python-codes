'''6. Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again
until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the
program will exit. Import random. '''
import random

target = random.randint(1, 9)
guess = int(input("Enter the number: "))
print(target)
if guess == target:
    print("You won!")
else:
    print("Try again!")

