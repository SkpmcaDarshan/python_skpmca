'''
3.Assume that a user enters any number and that the number is stored in the variable 
userNumber. Write a line of code that converts the input to a float. Then write a line of code 
that prints the positive value of the user’s input.
'''

userNumber = input("Enter the Number : ")

#convert into float

number = float(userNumber)

#print entered number

print("The Entered number is : ", number)

print("The positive number = ", abs(number))