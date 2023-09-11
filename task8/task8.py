# A simple function
def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}")

favorite_movie("The Shawshank Redemption")


# Creating a dictionary
def make_country(name, capital):
    country = {
        'name': name,
        'capital': capital
    }
    return country

country_dict = make_country('Ukraine', 'Kyiv')
print(country_dict)


# A simple calculator
def make_operation(operator, *args):
    result = args[0] if args else 0

    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num

    return result

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))