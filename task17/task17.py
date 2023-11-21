# Task 1

class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('Woof woof')


class Cat(Animal):
    def talk(self):
        print('Meow')


def animal_talk(animal_instance):
    animal_instance.talk()


dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)


# Task 2

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        author.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    num_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return f"Book: {self.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}', books={self.books})"

    def __str__(self):
        return f"Author: {self.name}"


library = Library("My Library")
author1 = Author("Author 1", "Country 1", "2000-01-01")
author2 = Author("Author 2", "Country 2", "1990-02-02")
book1 = library.new_book("Book 1", 2020, author1)
book2 = library.new_book("Book 2", 2021, author1)
book3 = library.new_book("Book 3", 2022, author2)

print(library.books)
print(library.group_by_author(author1))
print(library.group_by_year(2021))
print(Book.num_books)

# Task 3

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)
    print(x < y)
    print(x > y)
