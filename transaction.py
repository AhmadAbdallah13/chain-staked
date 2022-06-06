import copy
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

    def to_json(self):
        return self.__dict__

    def assign_signature(self, signature):
        self.signature = signature

    def payload(self) -> dict:
        """
        to check the is_signature_valid correctly we have to calculate the hash of the
        transaction object with the signature value as empty string, to get the same hash
        we calculated before.
        :return: dictionary object
        """
        json_rep = copy.deepcopy(self.to_json())
        json_rep["signature"] = ""
        return json_rep
