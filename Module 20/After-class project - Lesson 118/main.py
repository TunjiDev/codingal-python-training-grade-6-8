#Write a Python program to find the symmetric difference between two sets.

#For reference - The symmetric difference of two sets is equal to the set of elements that are in either of the sets but not in their intersection. In Python, you can use Set1.symmetric_difference(Set2)to find the symmetric of Set 1 and 2.

#Example - Set 1 = {1,2,3} and Set 2 = {3,4}
#Symmetric difference = {1,2,4}

#Find Symmetric Difference for :

#A. Set1 = {'blue', 'green'} Set2 = {'blue', 'yellow'}
#B. Set1 = {1, 2, 3, 4, 5} Set2 = {1, 5, 6, 7, 8, 9}

def find_symmetric_difference(set1, set2):
    # Calculate the symmetric difference between set1 and set2
    sym_diff = set1.symmetric_difference(set2)
    return sym_diff

# Set A: {'blue', 'green'} and {'blue', 'yellow'}
set1_A = {'blue', 'green'}
set2_A = {'blue', 'yellow'}
sym_diff_A = find_symmetric_difference(set1_A, set2_A)

# Set B: {1, 2, 3, 4, 5} and {1, 5, 6, 7, 8, 9}
set1_B = {1, 2, 3, 4, 5}
set2_B = {1, 5, 6, 7, 8, 9}
sym_diff_B = find_symmetric_difference(set1_B, set2_B)

# Print results
print(f"Symmetric difference of Set1 and Set2 (A): {sym_diff_A}")
print(f"Symmetric difference of Set1 and Set2 (B): {sym_diff_B}")