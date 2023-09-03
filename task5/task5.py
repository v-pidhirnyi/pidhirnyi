# The Guessing Game

import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations! You won!")
        break
    else:
        print("Nope, sorry. Try again!")

# The birthday greeting program

name = input("Enter name: ")
age = int(input("Enter age: "))

age = age + 1
print("Hello, " + name + ", on your next birthday you'll be " + str(age) + " years.")
