
class TransactionsPool:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction) -> None:
        """
        add a transaction to the transactions pool.
        :param transaction:
        :return: None
        """
        self.transactions.append(transaction)

    def transaction_exists(self, transaction_uuid) -> bool:
        """
        check if a transaction is already added in the transactions pool.
        :param transaction_uuid:
        :return: bool
        """
        for transaction in self.transactions:
            if transaction.equals(transaction_uuid):
                return True
        return False
