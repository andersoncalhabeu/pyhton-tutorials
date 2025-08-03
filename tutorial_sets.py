# Python Tutorial: Sets

# 1. Creating Sets
# You can create a set by using curly braces {} or the set() function
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Sets automatically remove duplicates!
numbers = {1, 2, 2, 3, 4}
print("Numbers set (duplicate 2 removed):", numbers)

# 2. Adding Elements
fruits.add("orange")
print("After adding 'orange':", fruits)

# 3. Update with Multiple Elements
fruits.update(["grape", "pear"])
print("After updating with ['grape', 'pear']:", fruits)

# 4. Removing Elements
fruits.remove("banana")  # Raises error if not present
print("After removing 'banana':", fruits)
fruits.discard("banana")  # Does nothing if not present
print("After discarding 'banana' again:", fruits)

# 5. Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print("Union:", set_a | set_b)  # Or set_a.union(set_b)

# Intersection
print("Intersection:", set_a & set_b)  # Or set_a.intersection(set_b)

# Difference
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference (elements in A or B, but not both)
print("Symmetric Difference:", set_a ^ set_b)

# 6. Membership Testing
print("Is 3 in set_a?", 3 in set_a)
print("Is 5 not in set_a?", 5 not in set_a)

# 7. Iterating through a Set
for fruit in fruits:
    print("Fruit in set:", fruit)

# 8. Convert set to list
fruits_list = list(fruits)
print("Fruits as list:", fruits_list)

# 9. Clearing and Deleting Sets
fruits.clear()  # Removes all elements
print("After clearing:", fruits)

# Deleting a set completely
del numbers
# print(numbers)  # This would raise an error because 'numbers' is deleted

# 10. Frozenset (an immutable set)
immutable_set = frozenset([1, 2, 3])
print("Frozenset:", immutable_set)

# Try adding an element to frozenset (will raise AttributeError)
# immutable_set.add(4)  # Uncomment to see the error

# End of tutorial!
print("End of set tutorial.")
