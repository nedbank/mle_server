from common.api import BaseController
from fastapi import APIRouter, HTTPException, Depends
from injector import inject
from transaction.infrastructure.services import TransactionService
from transaction.api.dto import InitiateTransactionDto

class TransactionController(BaseController):
    @inject
    def __init__(self, service: TransactionService):
        super().__init__(service)
        self.service = service
        self.router = APIRouter()
        self.create_routes()

    def create_routes(self):
        @self.router.post("/transaction")
        #@self.handle_exceptions
        async def initiate(transaction: InitiateTransactionDto):
            self.service.initiate(transaction)
            return {"message": "Transaction created"}

        @self.router.post("/transaction/{transaction_id}/status")
        @self.handle_exceptions
        def add_status(transaction_id: str, status: str):
            self.service.add_status(transaction_id, status)
            return {"message": "Status added"}

        @self.router.get("/transaction/{transaction_id}")
        @self.handle_exceptions
        def get_transaction(transaction_id: str):
            transaction = self.service.get_transaction(transaction_id)
            return transaction.to_dict()
