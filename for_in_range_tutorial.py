# Basic example of a for loop iterating over a list
frutas = ['apple', 'banana', 'orange', 'grape', 'kiwi']
for fruta in frutas:
    print(fruta)  # For each 'fruta' in the list 'frutas', print its value

print("\n--- loop with range() ---")

# Basic use of range to generate a numeric sequence from 0 to 4
for i in range(5):
    print(i)  # Prints numbers from 0 to 4 (range goes from 0 up to n-1)

print("\n--- loop with range(start, stop) ---")

# Range with defined start and end (from 3 up to 7, excluding 7)
for i in range(3, 7):
    print(i)  # Prints 3, 4, 5, 6

print("\n--- loop with range(start, stop, step) ---")

# Range with a defined step (start=2, stop=10, step=2)
for i in range(2, 10, 2):
    print(i)  # Prints 2, 4, 6, 8

print("\n--- loop with string ---")

# Iterating over the characters of a string
for letra in "python":
    print(letra)  # Prints each letter from the word "python" on a separate line

print("\n--- using for to iterate indices and access list ---")

# Using range and len to iterate indices and access list elements
for i in range(len(frutas)):
    print(f"Index {i}: {frutas[i]}")  # Displays index and corresponding fruit

print("\n--- for loop with break ---")

# Example of using break to exit the loop before it finishes
for i in range(10):
    if i == 5:
        print("Reached 5, exiting the loop.")
        break  # Exits the loop as soon as i equals 5
    print(i)

print("\n--- for loop with continue ---")

# Example of using continue to skip a specific iteration
for i in range(6):
    if i == 3:
        print("Skipping 3")
        continue  # Skips the rest of the current iteration when i == 3
    print(i)

print("\n--- for loop with else ---")

# The else block in a for loop is executed if the loop finishes normally (no break)
for i in range(3):
    print(i)
else:
    print("Loop finished without interruption")

print("\n--- nested for loop ---")

# Example of nested for loops for combinations
cores = ['red', 'blue', 'green']
formas = ['circle', 'squre', 'triangle']
for cor in cores:
    for forma in formas:
        print(f"{cor} {forma}")

print("\n--- list comprehension with for ---")

# Example of list comprehension to create a list of squares
quadrados = [x**2 for x in range(6)]
print("Squares:", quadrados)

print("\n--- summary ---")
print("""
- The for loop iterates over all elements of a sequence (list, string, etc).
- range() generates a sequence of numbers, ideal for index-controlled loops.
- break immediately stops the loop.
- continue skips to the next iteration of the loop.
- else on a for loop runs if the loop completes without a break.
- For loops can be nested for multiple dimensions.
- List comprehensions use for loops to create lists concisely.
""")
