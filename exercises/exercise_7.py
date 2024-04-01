# Exercise 7
integer = int(input("Enter a 4 digit number: "))

first_num = integer // 1000
second_num = ((integer // 100) % 10)
third_num = ((integer // 10) % 10)
fourth_num = integer % 10

print(first_num + second_num + third_num + fourth_num)
