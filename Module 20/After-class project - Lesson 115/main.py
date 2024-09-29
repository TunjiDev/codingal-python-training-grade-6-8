#Create a list of square value of numbers between specified range by the user, and then seperate the odd and even values.
#Write a function that accepts beginning and end range of numbers, and find the square values of those numbers. 
# Then filter the odd and even sqaure values and print them.


def square_values_and_filter(begin, end):
    # Calculate the square values of numbers in the given range
    squares = [num ** 2 for num in range(begin, end + 1)]
    
    # Separate odd and even square values
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]
    
    # Print the results
    print(f"Square values of numbers from {begin} to {end}: {squares}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

# Get input from the user
begin = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))

# Call the function
square_values_and_filter(begin, end)