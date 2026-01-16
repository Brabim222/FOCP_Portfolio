# Practical 02 – Variables, Strings, Lists

total = 100
print("The total is", total)

total += 99
print("The total is now", total)

total -= 1
total *= 4
total /= 2
print("Final total:", total)

# Average
total = 98.2
count = 5
average = total / count
print("Average:", average)

# Data types
print(type(100))
print(type(100.5))
print(type("Hello"))

# Input example (commented for safety)
# age = int(input("Enter age: "))
# print(age + 1)

# Strings
surname = "Palin"
print(surname[2])
print(surname[1:])

# Lists
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names.append("Brian")
print(names)

primes = [2,3,5,7,11,13,17]
print(primes[:4])
