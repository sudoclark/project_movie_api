from .base_error import BaseError

class ApiKeyError(BaseError):
    def __init__(self, message: str):
        super().__init__(message, type="API Error", status_code=401)