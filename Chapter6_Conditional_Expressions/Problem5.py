# Write a program which finds out whether a given name is present in a list or not.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Enter a number you want to find: "))

if(num in l):
    print("Number found")

else:
    print("Number not found")


l2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

name = input("Enter a name you want to find: ")

if (name in l2):
    print("Name found")

else:
    print("Name not found")