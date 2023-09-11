# Task 1
def count_words(sentence):

    words = sentence.lower().split()

    word_counts = {}

    for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


sentence = input("Enter a sentence: ")

word_counts = count_words(sentence)
print(word_counts)


# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0
for item, quantity in stock.items():
    if item in prices:
        total_price += prices[item] * quantity

print("The total price of the stock is:", total_price)


# Task 3
result = [(i, i**2) for i in range(1, 11)]
print(result)


# Task 4
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

weekdays_dict = {i+1: day for i, day in enumerate(weekdays)}

reverse_weekdays_dict = {day: i+1 for i, day in enumerate(weekdays)}

print(weekdays_dict)
print(reverse_weekdays_dict)