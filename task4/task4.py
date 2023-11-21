# String manipulation
def string1(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]


print(string1('Python'))

# The valid phone number program

number = (input("Write a mobile number: "))
if len(number) == 10 and number.isdigit():
    print("All good")
else:
    print("Your number is not correct!")

# The math quiz program

import random

first_number = random.randint(1, 10)
second_number = random.randint(1, 10)

operators = "+-/*"
operator = random.choice(operators)

raw_guess = input(
    f"""
    Please enter answer for expression 
    (use period and one digit after period if needed): 
    {first_number} {operator} {second_number}\n
    """
)

guess = None

while True:
    try:
        guess = float(raw_guess)
        break
    except ValueError as exception:
        raw_guess = input("Wrong format, please try again")


def expression(operand_1, operand_2, raw_operator):
    if raw_operator == "+":
        return operand_1 + operand_2
    elif raw_operator == "-":
        return operand_1 - operand_2
    elif raw_operator == "/":
        return operand_1 / operand_2
    elif raw_operator == "*":
        return round(operand_1 * operand_2, 1)


right_answer = round(expression(first_number, second_number, operator))
if guess == right_answer:
    print("Correct, well done!")
else:
    print(f"Wrong, correct answer is: {right_answer}")

# The name check

stored_name = "vitalii"
user_input = input("Please enter your name: ")

if user_input.lower() == stored_name:
    print("True")
else:
    print("False")

