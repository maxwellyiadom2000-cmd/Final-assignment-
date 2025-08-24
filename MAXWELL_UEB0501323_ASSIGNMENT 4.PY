import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Keep asking until the user guesses correctly
while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right. The number was {secret_number}.")
            break
    except ValueError:
        print("⚠ Please enter a valid number.")
