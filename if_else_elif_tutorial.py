# Tutorial: Using if, elif, and else statements in Python
# Ask the user for their age
age = int(input("Please enter your age: "))

# Using if-elif-else to check voting eligibility and age groups
if age < 0:
    print("Invalid age entered.")
elif age < 18:
    print("You are not old enough to vote yet.")
elif age == 18:
    print("Congratulations on reaching voting age this year!")
else:
    print("You are old enough to vote!")

# Explanation:
# - The program checks conditions in order.
# - If the first condition is False, it moves to the next `elif`.
# - If none of the above conditions are True, it runs the `else` block.
