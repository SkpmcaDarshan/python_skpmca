'''
Write a Python program that prompts the user for the cost of two items to be purchased. Then
prompt the user for their payment. If they enter an amount that is less than the total cost of
the two items, print a message that tells them how much they still owe. Otherwise, print a
message that thanks them for their payment and tells them how much change they will
receive. Thoroughly test your code for all possible input.
'''

print("="*40)
print("Welcome to the Store")
print("="*40)

# taking user input for the cost
item1_cost = float(input("Enter the cost of the first item: Rs"))
item2_cost = float(input("Enter the cost of the second item: Rs"))
total_cost = item1_cost + item2_cost

# user input for payment
payment = float(input("Enter your payment: Rs"))

# check that payment is less than total cost or not 
if payment < total_cost:
    # calculate the amoung still owe
    still_owed = total_cost - payment
    print(f"You still owe Rs{still_owed:.2f}")

else:
    # Calculate the change
    change = payment - total_cost
    print(f"Thank you for your payment. Your change is Rs{change:.2f}.")

print("="*40) 