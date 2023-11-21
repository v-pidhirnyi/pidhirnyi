# Task 1

import re


class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not self.email:
            raise ValueError("Email cannot be empty")

        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(regex, self.email):
            raise ValueError("Invalid email format")
        else:
            print(f"Email '{self.email}' is valid")


try:
    email_validator = EmailValidator("example@example.com")
except ValueError as e:
    print(e)

try:
    email_validator = EmailValidator("invalid_email.com")
except ValueError as e:
    print(e)

try:
    email_validator = EmailValidator("")
except ValueError as e:
    print(e)


# Task 2

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Can only add instances of Worker")

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        raise AttributeError("Cannot set workers directly. Use add_worker method.")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self._boss = value
            value.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class")


# Task 3

from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper

# Example usage:


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
