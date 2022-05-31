from Transactions import Transaction


if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"
    
    transaction = Transaction(sender, receiver, amount, transaction_type)
    print(transaction)
