# Exercise 1
user_number = int(input("Enter a 5 digit number: "))

first_number = (user_number // 10000) + (user_number // 100) % 10) + (user_number % 10)
second_number = (user_number // 1000) % 10) + (user_number // 10) % 10)

print(str(first_number) + str(second_number))
