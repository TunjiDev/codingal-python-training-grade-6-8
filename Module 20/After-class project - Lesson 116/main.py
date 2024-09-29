#Write a Python program to calculate the product, multiplying all the numbers of the given tuple.
import math

def multiply_tuple_elements(tup):
    product = 1
    for num in tup:
        product *= num
    return product

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate the product of each tuple
product_tup1 = multiply_tuple_elements(tup1)
product_tup2 = multiply_tuple_elements(tup2)

# Print the results
print(f"Product of the elements in tup1: {product_tup1}")
print(f"Product of the elements in tup2: {product_tup2}")