'''9. Write a Python program to develop a rock paper scissors game, restart the game until the user
press ‘n’ when the game ends. '''
import random
choices=["rock","paper","scissors"]
while True:
        user=input("enter any option").lower()
        computer=random.choice(choices)
        print(computer)
        if user==computer:
            print("its a tie")
        elif (user=="rock" and computer=="scissors")or\
            (user=="paper"and computer=="rock") or\
            (user=="scissors"and computer=="paper"):
            print("you won")
        else:
            print("you loose")

# import random
# choices=["rock","paper","scissors"]
# while True:
#         user=int(input('1.rock\n2.paper\n3.scissors'))
#         computer=random.choice(choices)
#         print(computer)
#         if user==computer:
#             print("its a tie")
#         elif (user=="rock" and computer=="scissors")or\
#             (user=="paper"and computer=="rock") or\
#             (user=="scissors"and computer=="paper"):
#             print("you won")
#         else:
#             print("you loose")
