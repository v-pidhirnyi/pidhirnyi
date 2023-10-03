# Task 1

def oops():
    raise IndexError("Oops! This is an IndexError")


def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except Exception as e:
        print(f"Caught an Exception: {e}")


catch_error()


def oops():
    raise KeyError("Oops! This is a KeyError")


def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except KeyError as e:
        print(f"Caught a KeyError: {e}")
    except Exception as e:
        print(f"Caught an Exception: {e}")


catch_error()

# Task 2
def squared_divided_by_b():
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))

        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        result = (a ** 2) / b
        return result
    except ValueError:
        print("Invalid input. Both a and b must be numbers.")
        return None
    except ZeroDivisionError as e:
        print(e)
        return None


result = squared_divided_by_b()

if result is not None:
    print(f"The result of squared a divided by b is: {result}")