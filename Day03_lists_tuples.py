# ==========================================
# Day 03: Lists & Tuples
# ==========================================

# 1. Lists Basics & Indexing/Slicing
# 2. List Methods (append, sort, reverse, insert, pop, remove)
# 3. Tuples Basics & Slicing
# 4. Tuple Methods (index, count)
# 5. Practice Questions

# 1. Lists Basics & Indexing/Slicing
marks = [85, 90, 78, 92, 88]
print("Original marks:", marks)
print("First element:", marks[0])
print("Slice (index 1 to 3):", marks[1:4])

# 2. List Methods (.append, .sort, .reverse, .copy)
fruits = ["apple", "banana"]
fruits.append("mango")
print("After append:", fruits)

fruits_copy = fruits.copy()
fruits_copy.reverse()
print("Reversed copy:", fruits_copy)

# 3. Practice Question 1: Favourite Movies List
movies = []
movies.append("Inception")
movies.append("Interstellar")
movies.append("The Dark Knight")
print("Favourite Movies:", movies)

# 4. Practice Question 2: Palindrome List Check
nums = [1, 2, 3, 2, 1]
nums_copy = nums.copy()
nums_copy.reverse()

if nums_copy == nums:
    print("nums list palindrome hai")
else:
    print("nums list palindrome nahi hai")

# 5. Tuples Basics & Methods (.count, .index)
grades = ("A", "B", "A", "C", "B", "A")
print("Grade A count:", grades.count("A"))
print("Index of first B:", grades.index("B"))

# Single element tuple with comma
single_tup = ("pawan",)
print("Single tuple type:", type(single_tup))