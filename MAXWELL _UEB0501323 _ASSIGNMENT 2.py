# Replace every uppercase letter with lowercase
s = "Hello"
print(s.lower())  # Output: hello


# Swap uppercase to lowercase and vice versa
s = "HeLLo WoRLd"
print(s.swapcase())  # Output: hEllO wOrlD


# Remove all uppercase letters
s = "HelloWorld"
result = "".join([ch for ch in s if not ch.isupper()])
print(result)  # Output: elloorld


# Count uppercase and lowercase letters
s = "EngiNEEr"
upper_count = sum(1 for ch in s if ch.isupper())
lower_count = sum(1 for ch in s if ch.islower())
print("Uppercase:", upper_count, ", Lowercase:", lower_count)
# Output: Uppercase: 4 , Lowercase: 4


import string

# Remove all non-English letters
s = "Data-Driven@2025!"
result = "".join([ch for ch in s if ch.isalpha()])
print(result)  # Output: DataDriven


# Heron’s formula for area of triangle
import math

a, b, c = 3, 4, 5
s = (a + b + c) / 2  # semi-perimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)  # Output: 6.0


# Format list of names in table form
names = ["John", "Elizabeth", "Mark", "Anna"]
print("Name".ljust(15), "Length".rjust(10))
print("-" * 25)
for n in names:
    print(n.ljust(15), str(len(n)).rjust(10))


import string

s = "   Hello, World!    "

# i. Remove leading/trailing whitespace
s = s.strip()

# ii. Replace all punctuation with empty string
s = "".join(ch for ch in s if ch not in string.punctuation)

# iii. Remove all spaces
s = s.replace(" ", "")

print(s)  # Output: HelloWorld
