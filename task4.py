# String manipulation
inputString = "Python"

count = 0

for i in inputString:
    count = count + 1
newString = inputString[0:2] + inputString[count - 2: count]

print("Input string = " + inputString)
print("New String = " + newString)

# The valid phone number program
