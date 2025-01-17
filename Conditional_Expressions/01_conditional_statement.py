#if elif elseif ladder

age = int(input("Enter your age: "))

if (age >= 18):
    print("You are an adult")

elif(age < 0):
    print("You are giving age less than 0; do you exists ?")

elif(age == 0):
    print("You are entering 0")

else: 
    print("You are minor")

print("End OF program")