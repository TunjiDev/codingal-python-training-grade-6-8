#Check the frequency of a value in the given test dictionary.

#Here's a test dictionary - {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
#Print this test dictionary and ask the user to enter the value for which they want to check the frequency (number of occurences) in the test dictionary. 
# Then print the frequency of that value.

# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test dictionary:", test_dict)

# Ask the user to input a value to check the frequency
value_to_check = int(input("Enter the value to check the frequency of: "))

# Count the frequency of the value in the dictionary
frequency = list(test_dict.values()).count(value_to_check)

# Print the frequency
print(f"The frequency of value {value_to_check} is: {frequency}")