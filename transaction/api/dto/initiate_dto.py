from pydantic import BaseModel

class InitiateTransactionDto(BaseModel):
    registration_no: str
    req_amount: float
    approved_amount:float
