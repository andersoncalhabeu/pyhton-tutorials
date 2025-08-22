# Tutorial: Lambda Functions in Python

# 1. What is a lambda function?
#    It's a small, anonymous function defined with the keyword 'lambda'.
#    General syntax: lambda arguments: expression

# Example: simple function that adds 10
add_ten = lambda x: x + 10
print("add_ten(5) =", add_ten(5))  # Output: 15

# Example: multiply two numbers
multiply = lambda x, y: x * y
print("multiply(3, 4) =", multiply(3, 4))  # Output: 12

# 2. Use with built-in functions like 'map'
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print("squared numbers:", squared)  # Output: [1, 4, 9, 16]

# 3. Use with 'filter' to select even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("even numbers:", evens)  # Output: [2, 4]

# 4. Use with 'sorted' to sort a list of tuples by the second value
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("sorted by second element:", sorted_pairs)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# 5. Lambda inside functions: returning a lambda
def make_incrementor(n):
    return lambda x: x + n

inc5 = make_incrementor(5)
print("inc5(10) =", inc5(10))  # Output: 15

# Bonus: Lambda vs. normal function
def add_five(x):
    return x + 5

add5_lambda = lambda x: x + 5

print("add_five(7) =", add_five(7))         # Output: 12
print("add5_lambda(7) =", add5_lambda(7))   # Output: 12

# Lambda functions are useful for short, simple operations, especially as arguments to higher-order functions.
