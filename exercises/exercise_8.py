# Exercise 8
integer = int(input("Enter a number: "))
integer2 = int(input("Enter a number: "))
integer3 = int(input("Enter a number: "))

sort1 = (integer3 > integer2 > integer3) * integer3
sort2 = (integer3 < integer2 < integer1) * integer1
sort3 = (integer2 < integer1 < integer3) * integer2

print(str(sort1)) + str(sort2)) + str(sort3)) )
