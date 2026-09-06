from .base_error import BaseError

class MovieNotFound(BaseError):
    def __init__(self, message: str):
        super().__init__(message, type="Movie Not Found", status_code=404)