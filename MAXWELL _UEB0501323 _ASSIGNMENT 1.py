# ASSIGNMENT 1 – REE 200 & PET ENG 200

# -----------------------------
# Task 1
# -----------------------------
# a. Create variables
integer_var = 10
float_var = 19.99
string_var = "Hello Petroleum"
boolean_var = True

# b. Print each variable with its type
print("Task 1:")
print(integer_var, type(integer_var))
print(float_var, type(float_var))
print(string_var, type(string_var))
print(boolean_var, type(boolean_var))
print("-" * 40)


# -----------------------------
# Task 2
# -----------------------------
print("Task 2:")
# a. Convert float 19.99 to integer
num1 = int(19.99)
print(num1, type(num1))

# b. Convert integer 50 to string
num2 = str(50)
print(num2, type(num2))

# c. Convert string “50” to float
num3 = float("50")
print(num3, type(num3))

# d. Each result and type printed above
print("-" * 40)


# -----------------------------
# Task 3
# -----------------------------
print("Task 3:")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello,", first_name, last_name + "!")
print("-" * 40)


# -----------------------------
# Task 4
# -----------------------------
print("Task 4:")
age = 20
# a. Fix the error by converting age to string
print("You are " + str(age) + " years old.")

# b. Explanation
print("Explanation: The error occurs because you cannot add (concatenate) a string and an integer directly in Python.")
print("-" * 40)


# -----------------------------
# Task 5
# -----------------------------
print("Task 5:")
fav_word = input("Enter your favourite word: ")
times = int(input("How many times should it be repeated? "))
print((fav_word + " ") * times)
print("-" * 40)


# -----------------------------
# Task 6
# -----------------------------
print("Task 6: Match the Errors")
print("a. print('Hello     -> C. SyntaxError")
print("b. int('abc')      -> A. ValueError")
print("c. 'age' + 10      -> B. TypeError")

