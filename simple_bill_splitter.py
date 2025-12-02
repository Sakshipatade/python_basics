'''
Takes total bill as input
Takes number of friends
Convert both to integers
Calculate each person’s share
Print: "Each person should pay: <amount>"
'''

total_bill = int(input("Your Total Bill: "))
total_friends = int(input("Total Friends: "))

Each_Payable_Amount = total_bill / total_friends

print("Each person should pay: ", int(Each_Payable_Amount))