# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
physics = int(input("physics :"))

# Let's calculate the percentage of marks
sum = math+english+science+physics
print("sun of math,english,science and physics")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)