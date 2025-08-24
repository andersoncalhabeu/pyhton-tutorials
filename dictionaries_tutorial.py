# Python Tutorial: Dictionaries

# 1. Creating Dictionaries
# You can create a dictionary with curly braces or the dict() function
person = {"name": "Alice", "age": 17, "city": "Ribeirão"}
print("Person dictionary:", person)

# 2. Accessing Values
print("Name:", person["name"])
print("Age:", person.get("age"))  # get() is safer, avoids KeyError

# 3. Adding or Updating Key-Value Pairs
person["email"] = "alice@example.com"
person["age"] = 31  # Update existing key
print("After adding/updating:", person)

# 4. Removing Items
del person["city"]  # Raises error if key not found
print("After deleting 'city':", person)
person.pop("email")  # Removes and returns value
print("After popping 'email':", person)

# 5. Dictionary Methods
# Keys, values, and items
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# 6. Iterating through a Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# 7. Checking for Keys
print("Does 'name' exist?", "name" in person)
print("Does 'city' exist?", "city" in person)

# 8. Nested Dictionaries
student = {
    "name": "Bob",
    "grades": {"math": 90, "science": 85}
}
print("Student's math grade:", student["grades"]["math"])

# 9. Copying a Dictionary
person_copy = person.copy()
print("Copy of person:", person_copy)

# 10. Clearing and Deleting Dictionaries
person.clear()
print("After clearing:", person)
del person_copy
# print(person_copy)  # This would raise an error because 'person_copy' is deleted

# 11. Dictionary Comprehension (Advanced)
squared = {x: x**2 for x in range(5)}
print("Dictionary comprehension (squares):", squared)

# End of tutorial!
print("End of dictionary tutorial.")

