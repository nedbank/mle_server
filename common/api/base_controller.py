import logging
from fastapi import APIRouter, HTTPException

class BaseController:
    def __init__(self, service):
        self.logger = logging.getLogger(__name__)
        self.service = service
        self.router = APIRouter()

    def create_routes(self):
        raise NotImplementedError("Not implemented")

    def handle_exceptions(self, func):
        def wrapper(*args, **kwargs):
            try:
                self.logger.log(*args)
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(e)
                raise HTTPException(status_code=500, detail=str(e))
        return wrapper
