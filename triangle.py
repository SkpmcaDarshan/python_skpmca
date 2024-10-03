'''
Create a Python program that prompts the user for a number and then prints an inverted right
triangle containing that many rows similar to the output to the right.
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''

num = int(input("Enter the number: "))

for  i in range(num, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


