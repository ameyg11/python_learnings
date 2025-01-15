#Write a program to input eight numbers from the user and display all the unique numbers (once)

s = set()

# for i in range(8):
#     a = input("Enter your favourite number : ")
#     s.add(a)

# print(s)

#Can we have a set with 18 (int) and '18' (str) as a value in it?

s = {18, '18'}

print(s)

#What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s)) # 2

#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

for i in range(4):
    name = input("Enter your name : ")
    lang = input("Enter your favourite language : ")
    d[name] = lang

print(d)