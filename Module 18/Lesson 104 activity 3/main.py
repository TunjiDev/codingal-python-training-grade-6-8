# Write a program that asks the user for a number n and prints the numbers from n to 1.
# enter a number greater than 1
n = int(input("Enter the value of n: "))

# print the numbers from n to 1
print("numbers from {0} to {1} are: ".format(n, 1))

#loop to print numbers from n to 1
for i in range(n, 0, -1):
   print(i)