#================================================
# Day 02: String & Conditional Statements
#================================================
# 1. Escape Sequence Characters
# 2. String Concatenation & len()
# 3. Indexing & Slicing
# 4. String Functions
# 5. Conditional Statements (if-elif-else)
 
#   1. Escape Sequence Characters
print("Hello\n world")   # \n se new line 
print("Name\t Pawan")    # \t se bada tabe space 

# 2. String Concatenation & len()
first_name = "Pawan"
last_name = "singh"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
print("Length:", len(full_name))

# Indexing & Slicing
world = "Pyhton"
print("First letter:",world[0])
print("Slicing (0 : 4):", world[0:4])

# 4. String Functions
msg = "i am learing python"
print("Ends with python?:", msg.endswith("python"))
print("Capitalize:", msg.capitalize())
print("Replace:", msg.replace("python","coding"))
print("Find 'l' :", msg.find("l"))
print("Count 'a':", msg.count("a"))

#  5. Conditional Statements (if-elif-else)
marks = int(input("Enter marks:"))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)
# ==================================
# Practice Questions
# ==================================
# Practice 1: User name input & length
user_name = input("Enter your first name: ")
print("Length of your name is:", len(user_name))

# Practice 2: Dollar sign '$' count
text = "The price is $50 and fee is $10"
print("Occurrence of $: ", text.count("$"))

# Practice 3: Odd or Even
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
