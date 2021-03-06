from block import Block
from transaction import Transaction
from transactions_pool import TransactionsPool
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"
    
    wallet = Wallet()
    fraudulent_wallet = Wallet()
    transactions_pool = TransactionsPool()

    transaction = wallet.create_transaction(receiver, amount, transaction_type)

    if not transactions_pool.transaction_exists(transaction.uuid):
        transactions_pool.add_transaction(transaction)

    if not transactions_pool.transaction_exists(transaction.uuid):
        transactions_pool.add_transaction(transaction)

    block = Block(transactions_pool.transactions, "prev_hash", "forger", 1)
    print("block is:", block.to_json(), sep='\n')
    print("the pool consists of:", transactions_pool.transactions, sep='\n')
