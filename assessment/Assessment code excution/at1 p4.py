import re

# Get user input
email = input("Enter Email ID: ")
password = input("Enter Password: ")

# Regex for Email ID
email_pattern = r'^[A-Za-z0-9]+[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$'

# Regex for Strong Password
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'

# Validate Email
if re.fullmatch(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")

# Validate Password
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Invalid Password")
