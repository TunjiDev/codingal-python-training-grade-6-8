# Write a Python program to generate random passwords consisting of lower case and upper case characters along with numbers. 
# You can also use random module for shuffling the password generated.

import random
import string

def generate_password(length):
    # Define character sets for lowercase, uppercase, and digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    
    # Ensure password contains at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase_letters + uppercase_letters + digits
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Convert the list of characters to a string
    return ''.join(password)

# Get password length from the user
password_length = int(input("Enter the desired password length: "))

# Generate and print the random password
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")