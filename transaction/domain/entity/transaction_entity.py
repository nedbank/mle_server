from transaction.api.dto import InitiateTransactionDto

class Transaction:
    def __init__(self, transaction:InitiateTransactionDto):
        self.registration_no= transaction.registration_no
        self.req_amount = transaction.req_amount
        self.approved_amount = transaction.approved_amount

    