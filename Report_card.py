# Report card of a student

# This message is shown at the beginning of the program
str = "Hey this is a report card of a brilliant student"
print(str)

# Taking the student's name as input
name = input("Enter name of a student :")

# Taking marks of all 5 subjects
marks_1 = int(input("Enter marks of your subject 1 :"))

marks_2 = int(input("Enter marks of your subject 2 :"))

marks_3 = int(input("Enter marks of your subject 3 :"))

marks_4 = int(input("Enter marks of your subject 4 :"))

marks_5 = int(input("Enter marks of your subject 5 :"))


# Finding the highest marks among all subjects
highest = max(marks_1,marks_2,marks_3,marks_4,marks_5)

# Finding the lowest marks among all subjects
lowest = min(marks_1,marks_2,marks_3,marks_4,marks_5)

# Displaying the highest and lowest marks
print("You got highest marks in :" , highest)
print("You got lowest marks in :" , lowest)

# Adding marks of all 5 subjects
sum = marks_1 + marks_2 + marks_3 + marks_4 + marks_5 

# Displaying the total marks
print("Your total marks are :", sum)

# Calculating percentage
Percentage = sum/5

# Displaying the percentage
print("Your percent is  :", Percentage)

# Checking the percentage and giving the grade
if Percentage >= 90: 
    print("You got Grade A")

# If percentage is between 75 and 89, grade B is given
elif Percentage >= 75 and Percentage< 90: 
    print("You got Grade B")

# If percentage is below 75, the student fails
else:
    print("Fail")
