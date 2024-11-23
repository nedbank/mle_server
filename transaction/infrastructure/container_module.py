from injector import Module, Binder
from transaction.infrastructure.services import TransactionService
from transaction.infrastructure.repositories import StatusRepository, TransactionRepository
from common.database import MongoTransaction

class TransactionModule(Module):
    def configure(self, binder: Binder):
        binder.bind(TransactionService, to=TransactionService)
        binder.bind(TransactionRepository, to=TransactionRepository)
        binder.bind(StatusRepository, to=StatusRepository)
        binder.bind(MongoTransaction, to=MongoTransaction)
