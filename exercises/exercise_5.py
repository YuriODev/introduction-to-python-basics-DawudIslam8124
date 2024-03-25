# Exercise 5
a = int(input("Enter integer one: "))
b = int(input("Enter integer two: "))

num_1_bigger = (a > b) * a
num_2_bigger = (b > a) * b

print(num_1_bigger + num_2_bigger)
