
marks_obtained = int(input("Enter marks obtained: "))

if (marks_obtained >= 90 and marks_obtained <=100):
    print("Grade Ex")

elif (marks_obtained >= 80 and marks_obtained <=90):
    print("Grade A")

elif (marks_obtained >= 70 and marks_obtained <=80):
    print("Grade B")

elif (marks_obtained >= 70 and marks_obtained <= 70):
    print("Grade C")

elif (marks_obtained >= 60 and marks_obtained <= 70):
    print("Grade D")

elif (marks_obtained < 0 or marks_obtained > 100):
    print("Invalid marks")

else:
    print("Grade F")