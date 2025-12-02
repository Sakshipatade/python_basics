'''
Has a stored username = "Sakshi"
Has a stored password = "1234"
Ask user to enter username and password
If both match → print "Login Successful!"
Otherwise keep asking again using a while loop
After 3 failed attempts → print "Account Locked" and stop
'''

user_name = "Sakshi"
password = 1234

count = 1
while(count <= 3):
    user_input_name = input("Enter Name: ")
    user_input_pass = int(input("Enter Password: "))

    if user_input_name == user_name and user_input_pass == password:
        print("login successful")
        break
    elif count == 3:
        print("Account Locked")
        break
    else:
        count = count + 1


        