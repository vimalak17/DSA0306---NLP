import re

# Compile the email pattern once
email_pattern = re.compile(
    r'^[A-Za-z0-9]+[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$'
)

# Sample email IDs
emails = [
    "vimala.kvv@gmail.com",
    "student1624@college.edu",
    "vimala@yahoo.in",
    "aishuab@company.org",
    "invalid@email",
    "@gmail.com",
    "test123@gmail.com"
]

# Validate each email
for email in emails:
    if email_pattern.fullmatch(email):
        print(email, "-> Valid Email")
    else:
        print(email, "-> Invalid Email")
