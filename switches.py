'''
5.Create a program which will allow the user to enter the state of two switches (either 1 (on) or 
0 (off)). The program should work out if both switches are on and then output the message 
'''

switch1 = int(input("Enter the state of switch 1 (1 for ON, 0 for OFF): "))
switch2 = int(input("Enter the state of switch 2 (1 for ON, 0 for OFF): "))

# Check if both switches are either 0 or 1
if (switch1 == 1 or switch1 == 0) and (switch2 == 1 or switch2 == 0):
    if switch1 == 1 and switch2 == 1:
        print(" Switch1   Switch2   On/Off")
        print("  " + str(switch1) + " "*10 + str(switch2) + " "*10 + "1")
    else:
        print(" Switch1   Switch2   On/Off")
        print("  " + str(switch1) + " "*10 + str(switch2) + " "*10 + "0")
else:
    print("Please enter either 0 or 1.")
