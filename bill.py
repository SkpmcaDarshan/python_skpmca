'''
2. Create a program the outputs the total cost of a lunch order. Users should be prompted to 
input the number of hamburgers, fries, and drinks they want and the program should print the 
total cost of the order. The hamburgers cost 2.00, fries cost 1.50, and drinks cost 1.00. Be 
creative and professional in prompting the user for the information and in displaying the 
output.
'''

hamburger_price = 2.00 
fries_price = 1.50
drinks_price = 1.00

print("Welcome to our shop : ")
print("Here is the menu : ")
print("  product          cost")
print("-"*40)
print("1.Hamburger        2.00")
print("2.Fries            1.50")
print("3.Drinks           1.00")

print("\nWhat is your order (add quantity): ")
print("  product               Quantity")
print("-"*40)
num_hamburger = int(input("1.Hamburger               : "))
num_fries = int(input("1.Fries                   : "))
num_drinks = int(input("1.Drinks                  : "))

hamburger_total = hamburger_price * num_hamburger
fries_total = fries_price * num_fries
drinks_total = drinks_price * num_drinks

total = hamburger_total + fries_total + drinks_total

print("\n     Your Order Summary     ")
print("-"*40)
print("  Product    Cost    Qty.    Total")
print("-"*40)
print("1.Hamburger  " + str(hamburger_price) + "     " + str(num_hamburger) + "       " + str(hamburger_total))
print("1.Fries      " + str(fries_price) + "     " + str(num_fries) + "       " + str(fries_total))
print("1.Drinks     " + str(drinks_price) + "     " + str(num_drinks) + "       " + str(drinks_total))
print("-"*40)
print("Total                       : " + str(total))
