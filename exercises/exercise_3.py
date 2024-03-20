# Exercise 3
n = int(input("Enter the number of seconds: "))

h = ((n // 3600) % 24)
m = ((n // 60 ) % 60)
s = n % 60

print( h,":",m,":",s,":")
