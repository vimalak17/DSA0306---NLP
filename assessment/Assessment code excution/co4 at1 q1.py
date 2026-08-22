print("=" * 60)
print("FRAME SEMANTICS IN BANKING")
print("=" * 60)

requests = [
    ("Transfer Rs.20,000 from my savings account to my son's account.",
     "TRANSFER(SourceAccount, Amount, DestinationAccount, Customer)"),

    ("Block my debit card immediately.",
     "BLOCK(DebitCard, Customer)"),

    ("Send my transaction statement to my email.",
     "SEND(TransactionStatement, Email, Customer)"),

    ("Increase my daily withdrawal limit.",
     "MODIFY(WithdrawalLimit, Customer)")
]

for query, frame in requests:
    print("\nCustomer Query:")
    print(query)
    print("Semantic Frame:")
    print(frame)

print("\nTASK 1")
print("""
Transfer:
Action = Transfer
Source = Savings Account
Amount = Rs.20,000
Destination = Son's Account
Customer = Account Holder

Block:
Action = Block
Object = Debit Card
Customer = Account Holder

Send:
Action = Send
Object = Transaction Statement
Destination = Email
Customer = Account Holder

Modify:
Action = Increase
Object = Withdrawal Limit
Customer = Account Holder
""")

print("TASK 2")
print("B4 is incorrect.")
print("Actual Intent: Increase withdrawal limit")
print("System Interpretation: Decrease withdrawal limit")
print("Reason: Increase and decrease have opposite meanings.")

print("\nTASK 3")
print("""
Incorrect semantic-role identification can cause the banking
system to perform the wrong operation.

For example, if increase withdrawal limit is interpreted as
decrease withdrawal limit, the customer's limit may be reduced.
""")

print("TASK 4")
print("""
A reliable banking NLP system should use:
1. Intent Classification
2. Named Entity Recognition
3. Semantic Role Labeling
4. Frame-Based Semantic Parsing
5. Business Rule Validation
6. Transaction Validation
7. Confirmation for important transactions
""")

print("=" * 60)
print("BANKING ANALYSIS COMPLETED")
print("=" * 60)
