# Exercise 6
a = int(input("Enter integer one: "))
b = int(input("Enter integer two: "))

divisible_yes = (a % b == 0) * "YES"
divisible_no = (a % b != 0) * "NO"

print(divisible_yes + divisible_no)
