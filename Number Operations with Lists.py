# Python Number Operations with Lists, Including: 
# Prime, Odd, Even, and Divisible-by-3 Filters

# 1. Creating a List of Numbers
numbers = [10, 3, 2.5, -7, 5, 20, 13, 9, 0]  # Mixed list
print("Original list:", numbers)

# 2. Filtering Functions

# Check if an integer is prime
def is_prime(n):
    if not isinstance(n, int) or n < 2:  # Only integers >=2 can be prime
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Find all prime numbers in the list
primes = [x for x in numbers if is_prime(x)]
print("\nPrime numbers in the list:", primes)

# Find all odd numbers in the list (integers only)
odds = [x for x in numbers if isinstance(x, int) and x % 2 != 0]
print("Odd numbers in the list:", odds)

# Find all even numbers in the list (integers only)
evens = [x for x in numbers if isinstance(x, int) and x % 2 == 0]
print("Even numbers in the list:", evens)

# Find numbers divisible by 3 (integers only)
div_by_3 = [x for x in numbers if isinstance(x, int) and x % 3 == 0]
print("Numbers divisible by 3 in the list:", div_by_3)

# 3. Usual number operations for comparison
addition = numbers[0] + numbers[1]
print("\nAddition (numbers[0] + numbers[1]):", addition)

subtraction = numbers[0] - numbers[1]
print("Subtraction (numbers[0] - numbers[1]):", subtraction)

multiplication = numbers[1] * numbers[2]
print("Multiplication (numbers[1] * numbers[2]):", multiplication)

division = numbers[0] / numbers[1]
print("Division (numbers[0] / numbers[1]):", division)

int_division = numbers[0] // numbers[1]
print("Integer Division (numbers[0] // numbers[1]):", int_division)

modulo = numbers[0] % numbers[1]
print("Modulo (numbers[0] % numbers[1]):", modulo)

# 4. List-wide operations
sum_all = sum([x for x in numbers if isinstance(x, (int, float))])
print("\nSum of all list elements:", sum_all)

average = sum_all / len(numbers)
print("Average of all list elements:", average)

# 5. Modifying the list
numbers[3] = abs(numbers[3])  # Making -7 positive
print("\nModified list:", numbers)

numbers.append(17)    # Add a new element to the end
print("After append(17):", numbers)

numbers.remove(3)     # Remove the first 3
print("After remove(3):", numbers)

# 6. Applying functions to list elements
import math
squared_list = [x**2 for x in numbers]
print("\nList of squares:", squared_list)

sqrt_list = [math.sqrt(abs(x)) for x in numbers]
print("List of square roots of abs values:", sqrt_list)

# 7. Summarize findings
print("\nSUMMARY:")
print("Primes:", primes)
print("Odds:", odds)
print("Evens:", evens)
print("Divisible by 3:", div_by_3)
