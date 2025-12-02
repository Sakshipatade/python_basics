'''
Ask user to enter PIN
If PIN length is not 4 → print "Invalid PIN"
Otherwise → welcome them using slicing:
Last 2 digits of PIN only
PIN = 9876 → output includes "Welcome user *76"
'''

PIN =input("Enter your 4 digit pin: ")
length_of_pin = len(PIN)
if length_of_pin != 4:
    print("Invalid PIN")
else:
    concatenated_string = "*"+PIN[-2:len(PIN)]
    print("WELCOME USER",concatenated_string)