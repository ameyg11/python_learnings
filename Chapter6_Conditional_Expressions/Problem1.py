# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if (a > b and a > c and a > d):
    print(f"Number a ({a}) is greatest")

elif (b > a and b > c and b > d):
    print(f"Number b ({b}) is greatest")

elif (c > a and c > b and c > d):
    print(f"Number c ({c}) is greatest")

else: 
    print(f"Number d ({d}) is greatest")
