from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from utils import Utils


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        hashed_data = Utils.hash(data)
        signature_scheme_object = PKCS1_v1_5.new(self.keyPair)
        signature = signature_scheme_object.sign(hashed_data).hex()
        return signature

    @staticmethod
    def signature_valid(data, signature, public_key_string):
        signature = bytes.fromhex(signature)
        data_hash = Utils.hash(data)
        public_key = RSA.importKey(public_key_string)
        signature_scheme_object = PKCS1_v1_5.new(public_key)
        return signature_scheme_object.verify(data_hash, signature)

    def get_public_key(self) -> str:
        return self.keyPair.public_key().exportKey("PEM").decode("utf-8")
