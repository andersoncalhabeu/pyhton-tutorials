# Basic example of a while loop
counter = 0                              # Set the initial value of the counter to 0
while counter < 5:                       # The loop will run while counter is less than 5
    print("Counter:", counter)           # Print the current counter value
    counter += 1                         # Increase counter by 1

print("\n--- While loop with condition ---\n")

# Example: asking for user input until a condition is met
secret = "python"                        # Set the secret word
guess = ""                               # Initialize the guess variable

while guess != secret:                   # Keep looping until the guess matches the secret
    guess = input("Guess the secret word: ")       # Ask for user input

print("You guessed it!\n")

# Using break inside a while loop
print("--- While loop with break ---\n")
i = 0                                   # Start at 0
while True:                             # Infinite loop (condition is always True)
    print(i)
    i += 1
    if i >= 3:                          # If counter reaches 3 or more,
        print("Breaking out of the loop.")
        break                           # Exit from the loop immediately

print("\n--- While loop with continue ---\n")

# Using continue to skip an iteration
j = 0
while j < 5:
    j += 1
    if j == 3:
        print("Skipping number 3")
        continue                        # Skip the rest of this iteration and go to the next
    print("Number:", j)

print("\n--- While loop with else ---\n")

# The else block runs if the while condition becomes False (not interrupted by a break)
number = 0
while number < 3:
    print("Inside while:", number)
    number += 1
else:
    print("Loop finished normally (no break).")

print("\n--- Common pitfall: Infinite loop (be careful!) ---\n")

# Uncomment the code below to see an infinite loop (NOT recommended for actual use)
# Example: infinite loop if you forget to update the variable in the condition
# k = 0
# while k < 3:
#     print("This will repeat forever if k is never incremented!")

print("Tutorial finished! Explore changing the conditions and values.")
