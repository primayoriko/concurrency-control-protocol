class Transaction:
    def __init__(self):
        self.priority = 0
        pass

    def get_prio(self):
        return self.priority

    def set_prio(self, prio):
        self.priority = prio

    def read(self, target):
        pass

    def write(self, target):
        pass

    def commit(self):
        pass

    def commit(self):
        pass

    @staticmethod
    def builder():
        pass