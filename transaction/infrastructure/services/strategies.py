from datetime import datetime
from transaction.domain.entity import TransactionStatus
from abc import ABC, abstractmethod


class BaseStatusStrategy(ABC):
    @abstractmethod
    def create_status(self) -> TransactionStatus:
        pass

class PendingStatusStrategy(BaseStatusStrategy):
    def create_status(self,transaction_id) -> TransactionStatus:
        return TransactionStatus(transaction_id,status="Pending")


class ProcessedStatusStrategy(BaseStatusStrategy):
    def create_status(self,transaction_id) -> TransactionStatus:
        return TransactionStatus(transaction_id,transaction_id,status="Processed")


class FailedStatusStrategy(BaseStatusStrategy):
    def create_status(self,transaction_id) -> TransactionStatus:
        return TransactionStatus(transaction_id,status="Failed")
