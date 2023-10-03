# Task 1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")


carl = Person("Carl", "Johnson", 26)
carl.talk()

# Task 2

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        human_equivalent_age = self.dog_age * self.age_factor
        return human_equivalent_age


dog1 = Dog(3)
print(f"Dog's age in human years: {dog1.human_age()}")

# Task 3

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_channel_index = N - 1
            return self.current_channel()
        else:
            return "No"

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, N_or_name):
        if isinstance(N_or_name, int):
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        elif isinstance(N_or_name, str):
            return "Yes" if N_or_name in self.channels else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))

