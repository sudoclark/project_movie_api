from .base_error import BaseError

class MovieNotFound(BaseError):
    """
    Exceção personalizada do sistema, ela é chamada quando o filme não foi encontrado.
    """
    def __init__(self, message: str):
        super().__init__(message, error_type="Movie Not Found", status_code=404)
