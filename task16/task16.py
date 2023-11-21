# Task 1

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and live at {self.address}.")


class Student(Person):
    def __init__(self, name, age, address, student_id, grade):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade = grade

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")


class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def teach(self, subject):
        print(f"{self.name} is teaching {subject}.")

    def get_salary(self):
        print(f"{self.name}'s salary is ${self.salary:.2f}")


person = Person("John Smith", 35, "123 Main St")
student = Student("Alice Johnson", 17, "456 Elm St", "S12345", "10th Grade")
teacher = Teacher("Mr. Brown", 45, "789 Oak St", "T9876", "Math", 55000.00)

person.introduce()
student.introduce()
student.study("Math")
teacher.introduce()
teacher.teach("Math")
teacher.get_salary()


# Task 2

class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]


math = Mathematician()

assert math.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert math.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert math.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Task 3

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type.")
        if amount <= 0:
            raise ValueError("Amount should be greater than zero.")
        product_with_premium = Product(product.type, product.name, product.price * 1.3)
        for existing_product in self.products:
            if existing_product.type == product_with_premium.type and existing_product.name == product_with_premium.name:
                existing_product.price = product_with_premium.price
                existing_product.amount += amount
                break
        else:
            product_with_premium.amount = amount
            self.products.append(product_with_premium)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0:
            raise ValueError("Discount percentage cannot be negative.")
        if identifier_type not in ['name', 'type']:
            raise ValueError("Invalid identifier_type. Use 'name' or 'type'.")
        for product in self.products:
            if identifier_type == 'name' and product.name == identifier:
                product.price *= (1 - percent / 100)
            elif identifier_type == 'type' and product.type == identifier:
                product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    return product.price * amount
                else:
                    raise ValueError(f"Not enough {product_name} in stock.")
        raise ValueError(f"{product_name} not found in the store.")

    def get_income(self):
        return sum((product.price * product.amount) for product in self.products)

    def get_all_products(self):
        return [(product.type, product.name, product.price, product.amount) for product in self.products]

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return (product.name, product.amount)
        raise ValueError(f"{product_name} not found in the store.")

# Test the code
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))

# Task 4

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")


try:
    raise CustomException("Something went wrong")
except CustomException as e:
    print(f"Custom Exception: {e}")
