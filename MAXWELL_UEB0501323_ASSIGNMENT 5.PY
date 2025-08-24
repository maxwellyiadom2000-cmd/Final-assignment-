def name():
    try:
        name = input('Enter your name: ')
        number = int(input('Enter your number: '))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("⚠ Invalid input. Please enter a valid number.")

name()
