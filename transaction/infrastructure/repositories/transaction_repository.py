from typing import Protocol, Optional
from transaction.domain.entity import Transaction
from common.database import MongoTransaction
from common.config import AppConfig
from injector import inject

COLLECTION = 'transaction'

class TransactionRepository(Protocol):
    @inject
    def __init__(self,db:MongoTransaction):
        self.client = db.get_client()

    async def save(self, transaction: Transaction) -> Transaction:
        self.collection = self.client[AppConfig.get_db_name](COLLECTION)
        return await self.collection.insert(transaction)

    def find_by_id(self, transaction_id: str) -> Optional[Transaction]:
        self.collection = self.client[AppConfig.get_db_name](COLLECTION)
        raise NotImplementedError('TransactionRepository is not implemented')
    
    def update(self, transaction: Transaction) -> Optional[Transaction]:
        self.db(COLLECTION,transaction)
        raise NotImplementedError('TransactionRepository is not implemented')