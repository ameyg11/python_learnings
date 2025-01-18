# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number: "))

for i in range(num,num*10+1,num):
    print(f"{num} * {i//num} = {i}")

for i in range(1,num+1):
    print(f"{num} * {i} = {num*i}")

print("****************")

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")