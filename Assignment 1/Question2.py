

def process_atm_transactions(balance):
    successful_transactions = 0
    while True:
        transaction_amount = float(input("Enter a transaction amount (0 to exit): "))
        if transaction_amount == 0:
            break
        elif transaction_amount > 0:
            balance += transaction_amount
            successful_transactions += 1
            print(f"Deposited: {transaction_amount}. New balance: {balance}.")
        else:
            if balance + transaction_amount >= 0:
                balance += transaction_amount
                successful_transactions += 1
                print(f"Withdrew: {-transaction_amount}. New balance: {balance}.")
            else:
                print("Insufficient funds.")
    return balance, successful_transactions

balance, transactions = process_atm_transactions(float(input("Enter your starting balance: ")))
print(f"Final balance: {balance}")
print(f"Number of transactions: {transactions}")
