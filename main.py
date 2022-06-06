from transaction import Transaction
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"
    
    wallet = Wallet()
    fraudulent_wallet = Wallet()

    transaction = wallet.create_transaction(receiver, amount, transaction_type)
    is_signature_valid = Wallet.signature_valid(
        transaction.payload(), transaction.signature, wallet.get_public_key()
    )
    is_signature_valid2 = Wallet.signature_valid(
        transaction.payload(), transaction.signature, fraudulent_wallet.get_public_key()
    )

    print("valid sig my man? ", is_signature_valid)
    print("my man, you're giving me the wrong public key? Say False if it's the wrong wallet ",
          is_signature_valid2)
