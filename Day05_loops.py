# ==========================================
# Day 05: Loops & Control Statements
# ==========================================

# 1. While Loop Basics
# 2. For Loop with Sequences (List, String)
# 3. Range Function (range(start, stop, step))
# 4. Loop Control Statements (break, continue)
# 5. Practice Questions


# 1. While Loop Basics
print("--- 1. While Loop ---")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Reverse countdown using while
i = 5
while i > 0:
    print("Countdown:", i)
    i -= 1


# 2. For Loop with Sequences
print("\n--- 2. For Loop with Sequences ---")
skills = ["Python", "Git", "VS Code", "Terminal"]
for skill in skills:
    print("Skill:", skill)

# Looping through a string
word = "Code"
for char in word:
    print("Character:", char)


# 3. Range Function
print("\n--- 3. Range Function ---")
# Even numbers from 2 to 10
print("Even numbers:")
for num in range(2, 11, 2):
    print(num, end=" ")
print()


# 4. Loop Control Statements (break, continue)
print("\n--- 4. Break and Continue ---")
# Continue: Skip number 3
print("Demonstrating continue (skips 3):")
for x in range(1, 6):
    if x == 3:
        continue
    print(x, end=" ")
print()

# Break: Stop loop when reaching 4
print("Demonstrating break (stops at 4):")
for y in range(1, 10):
    if y == 4:
        break
    print(y, end=" ")
print()


# 5. Practice Questions
print("\n--- 5. Practice Questions ---")

# Question 1: Print multiplication table of 5
number = 5
print(f"Table of {number}:")
for mul in range(1, 11):
    print(f"{number} x {mul} = {number * mul}")

# Question 2: Sum of first 10 natural numbers using while loop
total_sum = 0
current = 1
while current <= 10:
    total_sum += current
    current += 1
print("Sum of numbers 1 to 10:", total_sum)