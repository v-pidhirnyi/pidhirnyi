# The greatest number
import random

numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(1, 100))
    i += 1

largest_number = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest_number:
        largest_number = numbers[i]
    i += 1

print("List of numbers:", numbers)
print("Largest number:", largest_number)


# Exclusive common numbers
import random

list1 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    list1.append(num)
    i += 1

list2 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    list2.append(num)
    i += 1

list3 = list(set(list1) & set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("List 3 (common integers without duplicates):", list3)


# Extracting numbers
numbers_list = []
result_list = []

i = 1
while i <= 100:
    numbers_list.append(i)
    i += 1

for num in numbers_list:
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)

print(result_list)