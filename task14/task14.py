# Task 1

def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([repr(arg) for arg in args] + [f"{key}={value!r}" for key, value in kwargs.items()])
        print(f"{func.__name__} called with {arg_str}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

result = add(4, 5)
results = square_all(1, 2, 3)

# Task 2

def stop_words(stop_word_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in stop_word_list:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Task 3

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Argument '{arg}' is not of type {type_}")
                    return False
                if len(str(arg)) > max_length:
                    print(f"Argument '{arg}' has length greater than {max_length}")
                    return False
                for symbol in contains:
                    if symbol not in str(arg):
                        print(f"Argument '{arg}' does not contain '{symbol}'")
                        return False
            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

