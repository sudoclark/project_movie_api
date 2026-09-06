from .base_error import BaseError

class BadRequestError(BaseError):
    def __init__(self, message: str):
        super().__init__(message, type="Bad Request", status_code=400)