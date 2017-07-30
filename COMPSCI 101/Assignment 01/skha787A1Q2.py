"""
Sabaoon Raza Khan - skha787
ID Number: 983957824

Program that simulates four transactions on a bank account.
"""

import random

balance = 11568

random_transaction_amount1 = random.randrange (100, 151)
random_number1 = random.randrange (-1, 2, 2)
transaction1 = random_transaction_amount1 * random_number1
new_balance1 = balance + transaction1

random_transaction_amount2 = random.randrange (100, 151)
random_number2 = random.randrange (-1, 2, 2)
transaction2 = random_transaction_amount2 * random_number2
new_balance2 = new_balance1 + transaction2

random_transaction_amount3 = random.randrange (100, 151)
random_number3 = random.randrange (-1, 2, 2)
transaction3 = random_transaction_amount3 * random_number3
new_balance3 = new_balance2 + transaction3

random_transaction_amount4 = random.randrange (100, 151)
random_number4 = random.randrange (-1, 2, 2)
transaction4 = random_transaction_amount4 * random_number4
new_balance4 = new_balance3 + transaction4

sum_of_transactions = str(transaction1 + transaction2 + transaction3 + transaction4)

equal_signs_length = len("Sum of transactions: $") + len(sum_of_transactions) + 1

print("Initial balance: $", balance, sep = "")
print("1: $", new_balance1, " (", transaction1, ")", sep = "")
print("2: $", new_balance2, " (", transaction2, ")", sep = "")
print("3: $", new_balance3, " (", transaction3, ")", sep = "")
print("4: $", new_balance4, " (", transaction4, ")", sep = "")

print("=" * equal_signs_length)
print("Sum of transactions: $", sum_of_transactions, sep = "")
print("=" * equal_signs_length)






