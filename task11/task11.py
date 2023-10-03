# Task 1
with open("myfile.txt", "w") as file:
    file.write("Hello file world!\n")


with open("myfile.txt", "r") as file:
    contents = file.read()


print(contents)

