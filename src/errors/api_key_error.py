from .base_error import BaseError

class ApiKeyError(BaseError):
    """
    Exceção personalizada do sistema. Ela trata o erro '401' vindo da API dos filmes, ocorre quando tem algum problema
    com a chave da API (API KEY).
    """
    def __init__(self, message: str):
        super().__init__(message, type="API Error", status_code=401)