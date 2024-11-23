from typing import Protocol, Optional
from transaction.domain.entity import TransactionStatus
from injector import inject

class StatusRepository(Protocol):
    @inject
    def __init__(self,):
        pass
    def save(self, status: TransactionStatus) -> None:
        raise NotImplementedError('Not implemented')

    def find_by_id(self, status_id: str) -> Optional[TransactionStatus]:
        raise NotImplementedError('Not implemented')

    def update(self, status: TransactionStatus) -> Optional[TransactionStatus]:
        raise NotImplementedError('Not implemented')