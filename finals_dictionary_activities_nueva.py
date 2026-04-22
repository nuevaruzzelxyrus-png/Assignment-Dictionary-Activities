# Ruzzel Nueva
# DICTIONARY ACTIVITIES (Key-value pairs)

# Activity 1: Fill in the Blanks
# Task: Access the "name" key to print Ana
print("\nActivity 1: Fill in the Blanks")
student = {
    "name": "Ana",
    "age": 20,
    "course": "IT"
}

print(student["name"]) # Ang sagot sa blank ay "name"

# Activity 2: Add and Update
# Task: Add "grade": 95 and change age to 21
print("\nActivity 2: Add and Update")
student = {"name": "Ana", "age": 20}

# Add "grade"
student["grade"] = 95

# Change age to 21
student["age"] = 21
print(student)

# Activity 3: Loop Through Dictionary
# Task: Print all keys and values
print("\nActivity 3: Loop Through Dictionary")
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

for key, value in car.items():
    print(f"{key} : {value}")

# Activity 4 (Challenge): Mini Phonebook

print("\nActivity 4 (Challenge): Mini Phonebook")

# Create dictionary of 3 people and their numbers
phonebook = {
    "Lyka": "09123456789",
    "Adrian": "09987654321",
    "Nicole": "09109876543"
}

# Ask user for a name
name_search = input("Enter a name to find their number: ")

# Print the number
if name_search in phonebook:
    print(f"The number of {name_search} is: {phonebook[name_search]}")
else:
    print("Name not found in the phonebook.")
