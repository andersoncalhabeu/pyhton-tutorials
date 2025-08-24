# Creating an initial list with some elements
lista = [10, 5, 7, 3, 20, 15]

# Display the original list
print("Original list:", lista)  # Shows the initial list

# Sorting the list in ascending order
lista.sort()
print("Sorted list:", lista)  # List after ascending sort

# Sorting the list in descending order
lista.sort(reverse=True)
print("Sorted list descending:", lista)  # List sorted from largest to smallest

# Accessing individual elements (indexing)
print("First element:", lista[0])  # First element of the list
print("Last element:", lista[-1])  # Last element of the list

# Accessing a slice of the list (slicing)
print("Elements from index 1 to 3:", lista[1:4])  # Slice of the list, elements from index 1 to 3

# Adding elements
lista.append(25)  # Adds the value 25 at the end of the list
print("After append(25):", lista)

lista.insert(2, 12)  # Inserts the value 12 at index position 2
print("After insert(2, 12):", lista)

# Removing elements
lista.remove(7)  # Removes the first occurrence of the value 7
print("After remove(7):", lista)

removed = lista.pop()  # Removes and returns the last element of the list
print("After pop():", lista)
print("Element removed with pop():", removed)

removed_index = lista.pop(1)  # Removes and returns the element at index 1
print("After pop(1):", lista)
print("Element removed with pop(1):", removed_index)

# Searching elements
exists = 20 in lista  # Checks if the value 20 is in the list
print("Is 20 in the list?", exists)

# Counting occurrences
lista.extend([10, 20, 10])  # Adds several elements, with repetitions
print("After extend:", lista)
count_10 = lista.count(10)  # Counts how many times the value 10 appears
print("Occurrences of value 10:", count_10)

# Replacing an element (assigning a value to an index)
lista[0] = 100  # Replaces the first element with 100
print("After modifying index 0 to 100:", lista)

# Slice assignment (replacing a slice of the list)
lista[2:4] = [55, 66]  # Replaces the elements at indices 2 and 3
print("After modifying slice [2:4]:", lista)

# Reversing the list
lista.reverse()
print("After reverse():", lista)

# Creating a copy of the list
copy_list = lista.copy()
print("Copy of the list:", copy_list)

# Clearing all elements in the list
lista.clear()
print("After clear():", lista)

# Lists with different data types
mixed_list = [1, "two", 3.0, True]
print("Mixed list:", mixed_list)

# Iterating over the list with a for loop
print("Iteration over mixed_list:")
for element in mixed_list:
    print("-", element)

# List comprehensions (creating a new list)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Squares of the numbers
print("Squares:", squares)

# Filtering with list comprehension
evens = [x for x in numbers if x % 2 == 0]  # Even numbers
print("Even numbers:", evens)

# Merging lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Adds all elements of list2 to the end of list1
print("Merged list (extend):", list1)

# Length of the list
length = len(list1)
print("Length of merged list:", length)

# Using sum function to add numeric elements
total = sum(list1)
print("Sum of elements:", total)

# Finding the maximum and minimum values
maximum = max(list1)
minimum = min(list1)
print("Maximum:", maximum)
print("Minimum:", minimum)

# Copying list using slicing
copy_slice = list1[:]
print("Copy via slicing:", copy_slice)

# Counting elements with a loop
counter = 0
for item in list1:
    counter += 1
print("Manual count of elements:", counter)

# Using enumerate to get index and value together
print("Index and value in merged list:")
for index, value in enumerate(list1):
    print(f"{index} -> {value}")

# Inserting elements with list multiplication
repeated_zeros = [0] * 5  # List with five zeros
print("List of repeated zeros:", repeated_zeros)

# Converting a string into a list
text = "python"
letters_list = list(text)
print("List of letters from the word 'python':", letters_list)
