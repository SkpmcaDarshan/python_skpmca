'''
 4.Calculate the circumference and area of a circle when the user enters a radius. Round the 
answers to 2 decimal places. The input and output should be user friendly. 
 '''
import math
 
radius = float(input("Please enter the radius of the circle: "))


circumference = 2 * math.pi * radius
area = math.pi * radius * radius

print("The circumference of the circle is: ", circumference)
print("The area of the circle is: ", area)
