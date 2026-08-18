#Report card of a student

str = "Hey this is a report card of a brilliant student"
print(str)

name = input("Enter name of a student :")
marks_1 = int(input("Enter marks of your subject 1 :"))

marks_2 = int(input("Enter marks of your subject 2 :"))

marks_3 = int(input("Enter marks of your subject 3 :"))

marks_4 = int(input("Enter marks of your subject 4 :"))

marks_5 = int(input("Enter marks of your subject 5 :"))


highest = max(marks_1,marks_2,marks_3,marks_4,marks_5)

lowest = min(marks_1,marks_2,marks_3,marks_4,marks_5)

print("You got highest marks in :" , highest)
print("You got lowest marks in :" , lowest)

sum = marks_1 + marks_2 + marks_3 + marks_4 + marks_5 
print("Your total marks are :", sum)

Percentage = sum/5
print("Your percent is  :", Percentage)

if Percentage >= 90: 
    print("You got Grade A")

elif Percentage >= 75 and Percentage< 90: 
    print("You got Grade B")

else:
    print("Fail")
