# main.py
from fastapi import FastAPI
from injector import Injector
from common.config import AppConfig
from transaction.api.controller.transaction_controller import TransactionController
from transaction.infrastructure.container_module import TransactionModule

injector = Injector([TransactionModule])

app = FastAPI()

transaction_controller = injector.get(TransactionController)
app.include_router(transaction_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=AppConfig.get_app_host(), port=float(AppConfig.get_app_port()))
