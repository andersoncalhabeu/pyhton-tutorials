# String Manipulation Tutorial in Python

# 1. Creating Strings
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multiline string."""

print(s1)
print(s2)
print(s3)

# 2. Concatenation
greeting = s1 + " " + s2
print("Concatenation:", greeting)

# 3. String Length
print("Length of greeting:", len(greeting))

# 4. Accessing Characters
print("First character:", greeting[0])
print("Last character:", greeting[-1])

# 5. Slicing Strings
print("First 5 characters:", greeting[:5])
print("Last 5 characters:", greeting[-5:])

# 6. Changing Case
print("Uppercase:", greeting.upper())
print("Lowercase:", greeting.lower())
print("Title Case:", greeting.title())

# 7. Stripping Whitespace
s4 = "   padded string   "
print("Stripped:", s4.strip())

# 8. Replacing Substrings
print("Replace 'World' with 'Python':", greeting.replace("World", "Python"))

# 9. Splitting and Joining
csv = "apple,banana,cherry"
fruits = csv.split(",")
print("Split:", fruits)
joined = "-".join(fruits)
print("Joined:", joined)

# 10. String Formatting
name = "Alice"
age = 30
print("Hello, {}! You are {} years old.".format(name, age))
print(f"Hello, {name}! You are {age} years old.")

# 11. Checking Substrings
print("'Hello' in greeting?", "Hello" in greeting)
print("'Python' not in greeting?", "Python" not in greeting)

# 12. Useful String Methods
sample = "python programming"
print("Starts with 'py':", sample.startswith("py"))
print("Ends with 'ing':", sample.endswith("ing"))
print("Count of 'p':", sample.count("p"))
print("Find 'gram':", sample.find("gram"))
nome= "Jane"
print(nome.center(10, "♥")) # Centers the string with hearts
print(nome.upper())  # Converts to uppercase
print(nome.lower())  # Converts to lowercase
print(nome.title())  # Converts to title case
print(nome.capitalize())  # Capitalizes the first letter
print(nome.ljust(10, "♥")) # Left justifies the string with hearts
print(nome.rjust(10, "♥")) # Right justifies the string with hearts
print(nome.swapcase())  # Swaps case of all characters
print(nome.replace("Jane", "John"))  # Replaces 'Jane' with 'John'
print(nome.split())  # Splits the string into a list
print(nome.split("a"))  # Splits the string at 'a'
print(nome.splitlines())  # Splits the string into lines
print(nome.startswith("J"))  # Checks if the string starts with 'J'
print(nome.endswith("e"))  # Checks if the string ends with 'e'
print(nome.isdigit())  # Checks if the string is a digit
print(nome.zfill(10))  # Pads with zeros
print(nome.isalpha())  # Checks if all characters are alphabetic
print(nome.isdigit())  # Checks if all characters are digits
print(nome.isalnum())  # Checks if all characters are alphanumeric
print(nome.islower())  # Checks if all characters are lowercase
print(nome.isupper())  # Checks if all characters are uppercase
print(nome.isspace())  # Checks if all characters are whitespace
print(nome.startswith("D"))  # Checks if the string starts with 'J'
print(nome.endswith("e"))  # Checks if the string ends with 'e'

greeting = "Hello, Jane! Welcome to Python."  # Define the greeting variable

# 13. Finding Substrings
print("Index of 'Jane':", greeting.find("Jane"))  # Returns the index of the first occurrence
print("Index of 'Python':", greeting.find("Python"))  # Returns -1 if not found
print("Index of 'Python' with rfind:", greeting.rfind("Python"))  # Returns the index of the last occurrence
print("Index of 'Python' with index:", greeting.index("Python"))  # Raises ValueError if not found  
print("Index of 'Python' with rindex:", greeting.rindex("Python"))  # Raises ValueError if not found
# 14. Checking for Digits and Alphanumeric
print("Is '12345' a digit?", "12345".isdigit())  # True
print("Is 'Hello123' alphanumeric?", "Hello123".isalnum())  # True
print("Is 'Hello World' alphanumeric?", "Hello World".isalnum())  # False
# 15. Checking for Whitespace
print("Is '   ' whitespace?", "   ".isspace())  # True
# 16. String Alignment
print("Centered:", greeting.center(20, '*'))  # Centers the string with asterisks
print("Left Justified:", greeting.ljust(20, '-'))  # Left justifies the string with dashes
print("Right Justified:", greeting.rjust(20, '-'))  # Right justifies the string with dashes
# 17. String Padding
print("Zero-padded:", "42".zfill(5))  # Pads with zeros
# 18. String Comparison
print("Comparing 'abc' and 'ABC':", "abc" == "ABC")
# 19. String Iteration
for char in greeting:
    print(char, end=' ')  # Prints each character in the greeting
# 20. String Escape Characters
print("Newline:\nTab:\tBackslash:\\")  # Demonstrates escape characters
# 21. String Formatting with f-strings
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")  # f-string formatting
# 22. String Formatting with format()
print("Hello, {}! You are {} years old.".format(name, age))  # format method
# 23. String Formatting with % operator
print("Hello, %s! You are %d years old." % (name, age))  # Old-style formatting
# 24. String Encoding and Decoding
encoded = nome.encode('utf-8')  # Encodes the string to bytes
decoded = encoded.decode('utf-8')  # Decodes the bytes back to string
print("Encoded:", encoded)
