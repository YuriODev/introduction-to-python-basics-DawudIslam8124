# Exercise 4
integer = int(input("Enter an integer: "))

first_num = ((integer // 1000) % 10)
second_num = ((integer // 100) % 10)
third_num = ((integer // 10) % 10)
fourth_num = integer % 10

result = (first_num == fourth_num) * (second_num == third_num)
print(result)
