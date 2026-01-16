# Practical 03 – Conditions and Loops

age = 30

if 18 <= age <= 30:
    print("You are still young!")

# Ternary
print("Adult" if age >= 18 else "Not adult")

# Loops
for i in range(2, 11, 2):
    print(i, "to the power of", i, "=", i ** i)

numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0

for n in numbers:
    if n > 100:
        print("Value over 100 found, stopping")
        break
    total += n
    print("Running total:", total)
else:
    print("All numbers processed")
