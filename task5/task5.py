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

# Words combination
import random

def create_random_strings(input_string, num_strings):
    random_strings = []

    for _ in range(num_strings):
        random_string = ''.join(random.sample(input_string, len(input_string)))
        random_strings.append(random_string)

    return random_strings


input_string = input("Enter a word: ")
num_strings = 5

random_strings = create_random_strings(input_string, num_strings)

print("Random strings generated from the input word:")
for random_string in random_strings:
    print(random_string)