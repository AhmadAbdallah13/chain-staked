import json
from Crypto.Hash import SHA256


class Utils:

    @staticmethod
    def hash(data):
        data_string = json.dumps(data)
        data_bytes = data_string.encode("utf-8")
        hashed_data = SHA256.new(data_bytes)
        return hashed_data
