from transaction.domain.entity import Transaction, TransactionStatus
from transaction.infrastructure.repositories import StatusRepository, TransactionRepository
from transaction.api.dto import InitiateTransactionDto
from injector import inject

class TransactionService:
    @inject
    def __init__(self, transaction_repository: TransactionRepository, status_repository:StatusRepository):
        self.transaction_repository = transaction_repository
        self.status_repository = status_repository

    async def initiate(self, initTransaction:InitiateTransactionDto):
        transaction = Transaction(initTransaction)
        return await self.transaction_repository.save(transaction)


    def add_status(self, transaction_id: str, status: str):
        transaction = self.transaction_repository.find_by_id(transaction_id)
        if not transaction:
            raise TransactionNotFoundError(f"Transaction {transaction_id} not found.")
        transaction.add_status(status)
        self.transaction_repository.save(transaction)

    def get_transaction(self, transaction_id: str) -> Transaction:
        transaction = self.transaction_repository.find_by_id(transaction_id)
        if not transaction:
            raise TransactionNotFoundError(f"Transaction {transaction_id} not found.")
        return transaction
