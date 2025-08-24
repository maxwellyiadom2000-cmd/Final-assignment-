import math
import random
import string

# -----------------------------
# ASSIGNMENT 1
# -----------------------------
def assignment1():
    try:
        print("\n--- ASSIGNMENT 1 ---")
        # Task 1
        my_integer = 25
        my_float = 19.5
        my_string = "Hello Python"
        my_boolean = True

        print(my_integer, type(my_integer))
        print(my_float, type(my_float))
        print(my_string, type(my_string))
        print(my_boolean, type(my_boolean))

        # Task 2
        num_float = 19.99
        num_int = int(num_float)
        print(num_int, type(num_int))

        num = 50
        num_str = str(num)
        print(num_str, type(num_str))

        str_num = "50"
        num_float2 = float(str_num)
        print(num_float2, type(num_float2))

        # Task 3
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        print("Hello,", first_name, last_name + "!")

        # Task 4
        age = 20
        print("You are " + str(age) + " years old.")

        # Task 5
        word = input("Enter your favourite word: ")
        times = int(input("How many times to repeat it? "))
        print((word + " ") * times)

        # Task 6
        print("a. SyntaxError")
        print("b. ValueError")
        print("c. TypeError")
        print("d. NameError")

    except Exception as e:
        print("Error in Assignment 1:", e)


# -----------------------------
# ASSIGNMENT 2
# -----------------------------
def assignment2():
    try:
        print("\n--- ASSIGNMENT 2 ---")

        # Task 1
        s = "Hello"
        print(s.lower())

        # Task 2
        s = "HeLLo WoRLd"
        print(s.swapcase())

        # Task 3
        s = "HelloWorld"
        result = "".join([ch for ch in s if not ch.isupper()])
        print(result)

        # Task 4
        s = "EngiNEEr"
        upper_count = sum(1 for ch in s if ch.isupper())
        lower_count = sum(1 for ch in s if ch.islower())
        print("Uppercase:", upper_count, ", Lowercase:", lower_count)

        # Task 5
        s = "Data-Driven@2025!"
        result = "".join([ch for ch in s if ch.isalpha()])
        print(result)

        # Task 6
        a, b, c = 3, 4, 5
        sp = (a + b + c) / 2
        area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
        print(area)

        # Task 7
        names = ["John", "Elizabeth", "Mark", "Anna"]
        print("Name".ljust(15), "Length".rjust(10))
        print("-" * 25)
        for n in names:
            print(n.ljust(15), str(len(n)).rjust(10))

        # Task 8
        s = "   Hello, World!    "
        s = s.strip()
        s = "".join(ch for ch in s if ch not in string.punctuation)
        s = s.replace(" ", "")
        print(s)

    except Exception as e:
        print("Error in Assignment 2:", e)


# -----------------------------
# ASSIGNMENT 3
# -----------------------------
def assignment3():
    try:
        print("\n--- ASSIGNMENT 3 ---")
        number = int(input("Enter the number for multiplication table: "))
        for i in range(1, 13):
            print(f"{number} × {i} = {number * i}")
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print("Error in Assignment 3:", e)


# -----------------------------
# ASSIGNMENT 4
# -----------------------------
def assignment4():
    try:
        print("\n--- ASSIGNMENT 4 ---")
        secret = random.randint(1, 100)
        print("I have chosen a number between 1 and 100. Can you guess it?")
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
                else:
                    print(f"🎉 Correct! The number was {secret}")
                    break
            except ValueError:
                print("Please enter a valid number.")
    except Exception as e:
        print("Error in Assignment 4:", e)


# -----------------------------
# ASSIGNMENT 5
# -----------------------------
def assignment5():
    try:
        print("\n--- ASSIGNMENT 5 ---")
        name = input("Enter your name: ")
        number = int(input("Enter your number: "))
        if number % 2 == 0:
            print(f"{name}, your number is even.")
        else:
            print(f"{name}, your number is odd.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print("Error in Assignment 5:", e)


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    assignment1()
    assignment2()
    assignment3()
    assignment4()
    assignment5()
