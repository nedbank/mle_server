from pymongo import MongoClient
from datetime import datetime
from transaction.domain.entity import Transaction, TransactionStatus
from common.config import AppConfig
from injector import inject

class MongoTransaction:
    @inject
    def __init__(self, ):
        self.client = MongoClient(f"mongodb+srv://{AppConfig.get_username()}:{AppConfig.get_user_password()}@{AppConfig.get_db_url()}")
    def get_client(self):
        return self.client
    

    # def save(self, collection:str, transaction: Transaction) -> Transaction:
    #     self.collection = self.client[AppConfig.get_db_name][collection]
    #     transaction_data = transaction.to_dict()
    #     self.collection.insert(
    #         transaction_data,
    #         upsert=True,
    #     )
    #     return transaction
