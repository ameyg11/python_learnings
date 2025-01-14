a = "ameygawade"
print(len(a))

b = a[0:4]
print(b)

print(a[1:6:2])
print(a.endswith("ad"))

print(a.upper())
print(a.lower())
print(a.find("ga"))
print(a.replace("gawade", "g"))

c = "hi my name is \"amey\""
print(c)

d = input("enter your name")

print("Good Afternoon "  +d.capitalize())

print(f"GOOD AFTERNOON {d}")

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "AMEY").replace("<|Date|>", "1 JAN"))