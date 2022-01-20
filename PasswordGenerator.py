import random
import string

randomLetters = (string.ascii_letters)

while True:
    try:
        number = int(
            input("Enter the amount of password you want to generate: "))
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("Please enter an integer!")

for c in range(number):
    password = " "
    for x in range(length):
        password += random.choice(randomLetters)
    print(password)
