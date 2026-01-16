#Task 2

import random

password = input("Enter your password: ")

if len(password) < 9:
    print("Password too short.")
    exit()

length = len(password)

for _ in range(3):
    check_position = random.randint(1, length)
    guess = input(f"\nEnter letter at position {check_position}: ")

    if guess == password[check_position - 1]:
        print("Correct")
    else:
        print("Security check failed.")
        exit()

print("Security check passed.")
