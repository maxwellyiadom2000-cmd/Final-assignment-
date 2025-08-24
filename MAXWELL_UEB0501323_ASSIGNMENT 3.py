# Multiplication table with user input

# take input from the user
number = int(input("Enter a number: "))

# table up to 12
for i in range(1, 13):
    result = number * i
    print(f"{number} * {i} = {result}")
