'''
    Asks the user for their full name.
    Automatically formats the username like this:
    Remove spaces
    Convert to lowercase
    Slice the first 8 characters
'''


name = input("Enter your First name and Last name: ")
trimmed_text = name.replace(" ", "")
lower_text = trimmed_text.lower()   
print(lower_text[0:9])

#replace method is used to remove the unwanted space