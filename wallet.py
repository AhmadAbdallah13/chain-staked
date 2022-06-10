from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from transaction import Transaction
from utils import Utils


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        """
        create a signature for the transaction related to this wallet.
        :param data:
        :return: string of hexadecimal number that represents the signature
        """
        hashed_data = Utils.hash(data)
        signature_scheme_object = PKCS1_v1_5.new(self.keyPair)
        signature = signature_scheme_object.sign(hashed_data).hex()
        return signature

    @staticmethod
    def is_signature_valid(data, signature, public_key_string):
        """
        validates the signature of a transaction.
        :param data: of the transaction payload
        :param signature: of a specific transaction
        :param public_key_string: of the related wallet
        :return: bool value
        """
        signature = bytes.fromhex(signature)
        data_hash = Utils.hash(data)
        public_key = RSA.importKey(public_key_string)
        signature_scheme_object = PKCS1_v1_5.new(public_key)
        return signature_scheme_object.verify(data_hash, signature)

    def get_public_key(self) -> str:
        return self.keyPair.public_key().exportKey("PEM").decode("utf-8")

    def create_transaction(self, receiver, amount, transaction_type):
        transaction = Transaction(
            self.get_public_key(),
            receiver,
            amount,
            transaction_type
        )
        signature = self.sign(transaction.payload())
        transaction.assign_signature(signature)
        return transaction
