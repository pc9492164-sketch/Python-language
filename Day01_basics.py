# =========================================================================================
# Day 01: Python Basics & Calculations
# Today i learn
# 1. input() se user data lena (by default text/string hota hai).
# 2. float() se text ko decimal number me convert krna (type Casting)
# 3. Python basic math operaters ( +, -, *, /)
# ==========================================================================================

#  Practice 1: sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("sum is :", num1 + num2)
print()
# practice 2: Area of a Square
side = float(input("Enter side of square: "))
print("Area of square is:" ,side * side)
print()
# practice 3: Average of 2 floting point numbers
f1 = float(input("Enter first float number: "))
f2 = float(input("Enter second float number: "))
print("Average is : ", (f1 + f2)/2)
print()
# practice 4: Comparison
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Is a greater than or equal to b?:", a>=b)


