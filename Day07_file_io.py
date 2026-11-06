# ===================================================
# Day 07: File Input / Output (I/O) in Python
# ===================================================

# 1. Reading a File ('r' mode)
# 2. Writing to a File ('w' mode)
# 3. Appending to a File ('a' mode)
# 4. With Syntax (Automatic file closing)
# 5. Deleting a File (os module)
# 6. Practice Questions


# --- 1. Writing to a File ('w' mode) ---
print("--- 1. Writing to a File ---")
f = open("practice.txt", "w")
f.write("Hi everyone\nwe are learning File I/O\n")
f.write("using Java.\nI like programming in Java.\n")
f.close()
print("practice.txt file written successfully.")


# --- 2. Reading a File ('r' mode) ---
print("\n--- 2. Reading a File ---")
f = open("practice.txt", "r")
data = f.read()
print("Full File Data:")
print(data)
f.close()

# Reading line by line
f = open("practice.txt", "r")
line1 = f.readline()
print("First Line:", line1.strip())
line2 = f.readline()
print("Second Line:", line2.strip())
f.close()


# --- 3. Appending to a File ('a' mode) ---
print("\n--- 3. Appending to a File ---")
f = open("practice.txt", "a")
f.write("Learning with Python is easy and powerful!\n")
f.close()
print("New line appended to practice.txt")


# --- 4. With Syntax ---
print("\n--- 4. Using 'with' Syntax ---")
with open("practice.txt", "r") as f:
    content = f.read()
    print("Content using 'with':\n", content.strip())


# --- 5. Practice Questions ---
print("\n--- 5. Practice Questions ---")

# Q1: Replace all occurrences of 'Java' with 'Python' in practice.txt
with open("practice.txt", "r") as f:
    text = f.read()

new_text = text.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_text)

print("[Q1] Successfully replaced 'Java' with 'Python'.")


# Q2: Search if the word 'learning' exists in practice.txt
def check_for_word(word):
    with open("practice.txt", "r") as f:
        file_data = f.read()
        if word in file_data:
            print(f"[Q2] '{word}' found in the file.")
        else:
            print(f"[Q2] '{word}' NOT found in the file.")

check_for_word("learning")


# Q3: Find in which line the word 'learning' occurs first
def check_for_line(word):
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"[Q3] '{word}' found at line number: {line_no}")
                return line_no
            line_no += 1
    return -1

check_for_line("learning")


# Q4: From a file containing comma-separated numbers, count even numbers
# Step 1: Create numbers.txt
with open("numbers.txt", "w") as f:
    f.write("1, 2, 45, 55, 86, 76, 12, 19, 30")

# Step 2: Read and count even numbers
count = 0
with open("numbers.txt", "r") as f:
    num_data = f.read()
    nums = num_data.split(",")
    for val in nums:
        if int(val.strip()) % 2 == 0:
            count += 1

print(f"[Q4] Total even numbers in numbers.txt: {count}")