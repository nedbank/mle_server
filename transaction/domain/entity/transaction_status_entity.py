from datetime import datetime

class TransactionStatus:
    def __init__(self, transaction_id, status):
        self.transaction_id = transaction_id
        self.name = status
        self.datetime = timestamp=datetime.utcnow()


    