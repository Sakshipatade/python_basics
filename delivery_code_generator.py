'''
Ask for city name
Ask for area name
Generate a delivery code using slicing:
First 3 letters of city → uppercase
Last 2 letters of area → lowercase
Output format: CITY-xy
'''

city = input("Enter City: ")
area = input("Enter Area: ")
number = input("Enter any 5 number: ") #here numbers are taken as string not 'number' datatype 

uppercase_value_city = city.upper()
lowercase_value_area = area.lower()
indexed_city = uppercase_value_city[:3]
indexed_area = lowercase_value_area[-2:len(lowercase_value_area)]
indexed_number = number[3:5]

s = indexed_city + indexed_number + indexed_area

print("Generated OTP: ", s)