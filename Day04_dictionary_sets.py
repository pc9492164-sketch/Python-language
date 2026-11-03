# ==========================================
# Day 04: Dictionaries & Sets
# ==========================================

# 1. Dictionary Basics & Accessing Values
# 2. Dictionary Methods (keys, values, items, get, update, pop)
# 3. Sets Basics & Operations (add, remove, discard, pop)
# 4. Set Mathematical Operations (union, intersection, difference)
# 5. Practice Questions

# 1. Dictionary Basics & Accessing Values
student = {
    "name": "Pawan",
    "course": "Python",
    "duration_days": 30,
    "city": "Ballia"
}

print("Original student dict:", student)
print("Access using key:", student["name"])
print("Access using get():", student.get("course"))

# 2. Dictionary Methods

# Adding & Updating elements
student["duration_days"] = 45
student.update({"marks": 92, "status": "active"})
print("After update:", student)

# Fetching keys, values, and key-value pairs
print("Dict keys:", list(student.keys()))
print("Dict values:", list(student.values()))
print("Dict items:", list(student.items()))

# Removing elements
removed_val = student.pop("status")
print("Removed value:", removed_val)
print("Dict after pop:", student)


# ------------------------------------------
# 3. Sets Basics & Operations
# ------------------------------------------
# Sets store unique, unordered elements (duplicates automatically removed)
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique set:", numbers)

# Adding and Removing
numbers.add(6)
print("After add(6):", numbers)

numbers.remove(3)       # Removes 3
numbers.discard(10)     # Safe remove: agar element na ho tab bhi crash nahi karega
print("After remove & discard:", numbers)


# 4. Set Mathematical Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)


# 5. Practice Questions

# Q1: Frequency of characters in a string using dictionary
text = "programming"
char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print("Q1 Char Frequency:", char_freq)

# Q2: Remove duplicate elements from a list using set
raw_scores = [85, 90, 78, 85, 92, 90, 88]
unique_scores = list(set(raw_scores))
print("Q2 Unique Scores:", unique_scores)

# Q3: Common elements between two lists using set intersection
list1 = ["python", "c++", "java", "git"]
list2 = ["git", "python", "sql", "html"]
common_skills = list(set(list1) & set(list2))
print("Q3 Common Skills:", common_skills)