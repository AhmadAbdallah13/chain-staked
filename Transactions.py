import uuid
import time


class Transaction:
    def __init__(self, sender_public_key, receiver_public_key, amount, transaction_type):
        self.senderPublicKey = sender_public_key
        self.receiver_public_key = receiver_public_key
        self.amount = amount
        self.transaction_type = transaction_type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ""

    def __str__(self):
        return f"{self.__dict__}"
