# ===================================================
# Day 08: Object-Oriented Programming (OOPs) - Part 1
# ===================================================

# 1. Class and Object Basics
# 2. Constructor (__init__ function)
# 3. Class Attributes vs Instance Attributes
# 4. Methods in Class
# 5. Static Methods (@staticmethod)
# 6. Practice Questions (Student Grade & Bank Account)


# --- 1. Class and Object Basics ---
print("--- 1. Class & Object Basics ---")

class Student:
    name = "Karan"

# Creating object (instance) of class
s1 = Student()
print("Student Name:", s1.name)


# --- 2. Constructor & Attributes ---
print("\n--- 2. Constructor (__init__) & Attributes ---")

class Car:
    # Class attribute (common for all objects)
    wheels = 4

    # Constructor (__init__)
    def __init__(self, brand, color):
        # Instance attributes (different for each object)
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "White")
car2 = Car("BMW", "Black")

print(f"Car 1: Brand = {car1.brand}, Color = {car1.color}, Wheels = {car1.wheels}")
print(f"Car 2: Brand = {car2.brand}, Color = {car2.color}, Wheels = {car2.wheels}")


# --- 3. Methods inside Class ---
print("\n--- 3. Class Methods ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Pawan", 21)
p1.introduce()


# --- 4. Static Methods (@staticmethod) ---
print("\n--- 4. Static Method ---")

class MathUtility:
    # Static method doesn't need 'self'
    @staticmethod
    def greet():
        print("Welcome to Python OOPs learning!")

MathUtility.greet()


# ===================================================
# Practice Questions
# ===================================================
print("\n--- 5. Practice Questions ---")

# Practice Q1: Student class that takes name and marks of 3 subjects, then calculates average
class StudentRecord:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(f"Hi {self.name}, your average score is: {avg:.2f}")

s_record = StudentRecord("Rahul", [95, 88, 92])
s_record.get_avg()


# Practice Q2: Bank Account class with debit, credit, and balance display methods
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    # Debit method
    def debit(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Available: ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"₹{amount} was debited. Current balance: ₹{self.balance}")

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} was credited. Current balance: ₹{self.balance}")

    # Display balance
    def print_balance(self):
        print(f"Account No: {self.account_no} | Balance: ₹{self.balance}")

print("\n[Bank Account Demo]")
acc1 = Account(10000, "AC102030")
acc1.print_balance()
acc1.debit(1500)
acc1.credit(3000)
acc1.print_balance()