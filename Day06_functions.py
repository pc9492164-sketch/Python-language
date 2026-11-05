# ==========================================
# Day 06: Functions & Recursion
# ==========================================

# 1. Function Definition & Calling
# 2. Function with Parameters & Return Values
# 3. Default Arguments & Keyword Arguments
# 4. Variable-length Arguments (*args, **kwargs)
# 5. Recursion Basics (Factorial & Countdown)
# 6. Practice Questions


# 1. Function Definition & Calling
print("--- 1. Function Definition & Calling ---")
def greet():
    print("Hello! Welcome to Day 06 of Python Journey.")

greet()


# 2. Function with Parameters & Return Values
print("\n--- 2. Parameters & Return Values ---")
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(15, 25)
print("Sum is:", sum_result)

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print("14 is:", check_even_odd(14))
print("27 is:", check_even_odd(27))


# 3. Default Arguments & Keyword Arguments
print("\n--- 3. Default & Keyword Arguments ---")
def student_info(name, course="Python", city="Ballia"):
    print(f"Student: {name} | Course: {course} | City: {city}")

student_info("Pawan")
student_info("Akash", course="Data Science", city="Lucknow")


# 4. Variable-length Arguments (*args, **kwargs)
print("\n--- 4. *args and *kwargs ---")
# *args allows multiple positional arguments
def calculate_total(*numbers):
    total = sum(numbers)
    return total

print("Total sum:", calculate_total(10, 20, 30, 40))

# **kwargs allows multiple key-value arguments
def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_profile(username="Pc9492164-sketch", role="Student", lang="Python")


# 5. Recursion Basics
print("\n--- 5. Recursion Basics ---")
# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 using recursion:", factorial(5))

# Countdown using recursion
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n, end=" ")
    countdown(n - 1)

print("Recursive Countdown:")
countdown(5)


# 6. Practice Questions
print("\n--- 6. Practice Questions ---")

# Question 1: Find maximum of three numbers using a function
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Max number is:", find_max(45, 89, 23))

# Question 2: Calculate power of a number (base^exponent)
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

print("2 raised to power 4 is:", power(2, 4)) 