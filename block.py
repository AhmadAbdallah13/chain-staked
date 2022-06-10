import time


class Block:

    def __init__(self, transactions, previous_hash, forger, block_count):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.forger = forger
        self.block_count = block_count
        self.timestamp = time.time()
        self.signature = ""

    def to_json(self):
        data = {
            "transactions": [transaction.to_json() for transaction in self.transactions],
            "previous_hash": self.previous_hash,
            "forger": self.forger,
            "block_count": self.block_count,
            "timestamp": self.timestamp,
            "signature": self.signature,
        }
        return data
