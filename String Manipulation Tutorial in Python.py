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