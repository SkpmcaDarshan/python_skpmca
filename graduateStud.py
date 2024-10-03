'''
Suppose you want to determine if a student is ready to graduate. The 3 criteria for graduation
are that the student has earned at least 120 credits, their major GPA is at least 2.0 and their
general GPA is also at least 2.0. Write a Python program to implement the above criteria.
'''

stdName = input("Enter your name: ")
stdCredits = int(input("Enter your total credits: "))
stdMajorGPA = float(input("Enter your major GPA: "))
stdGeneralGPA = float(input("Enter your general GPA: "))

if stdCredits >= 120 and stdMajorGPA >= 2.0 and stdGeneralGPA >= 2.0:
    print(f"{stdName} is ready to graduate.")
else:
    print(f"{stdName} is not ready to graduate.")

