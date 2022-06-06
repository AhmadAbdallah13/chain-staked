from transaction import Transaction
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"
    
    transaction = Transaction(sender, receiver, amount, transaction_type)
    wallet = Wallet()

    signature = wallet.sign(transaction.to_json())
    transaction.sign(signature)

    is_signature_valid = Wallet.signature_valid(
        transaction.payload(), signature, wallet.get_public_key()
    )

    print("My man, is the signature valid?", is_signature_valid)
