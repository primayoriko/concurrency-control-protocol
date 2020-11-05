class TransactionManager:
    def __init__(self):
        self.transactions = [] 
        self.items = []
        pass

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_items(self, item):
        self.items.append(item)

    def get_lock(self):
        pass

    def release_lock(self):
        pass