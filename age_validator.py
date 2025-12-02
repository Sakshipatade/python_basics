'''
Takes user input for age (string).
Convert it to integer using type casting.
If age < 18 → print "You are not eligible."
Otherwise → print "Registration successful."
'''

user_age = int(input("Enter your age: "))

if user_age < 18:
    print("You are not eligible")
else:
    print("Registration successful")