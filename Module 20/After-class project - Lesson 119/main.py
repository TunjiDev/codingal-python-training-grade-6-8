# Perform List Comprehension to get mentioned results.

# List Comprehension enormously reduces time to process information in comparison to operators. Use List comprehension to do following - 
# 1. Take a number from user, create a list with all the odd numbers under the input value and other list of odd numbers.
# 2. Create a list of fruits. Then, convert the first letter of every element to capital and create a new list updated values.

# Task 1: Generate lists of odd and even numbers under the input value
user_input = int(input("Enter a number: "))

# List comprehension for odd numbers
odd_numbers = [num for num in range(user_input) if num % 2 != 0]

# List comprehension for even numbers
even_numbers = [num for num in range(user_input) if num % 2 == 0]

# Print the results
print(f"Odd numbers under {user_input}: {odd_numbers}")
print(f"Even numbers under {user_input}: {even_numbers}")


# Task 2: Capitalize the first letter of each fruit
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# List comprehension to capitalize the first letter
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Print the new list with capitalized first letters
print("Capitalized fruits:", capitalized_fruits)
