from .base_error import BaseError

class BadRequestError(BaseError):
    """
    Exceção personalizada usada para tratamento de erros vindos do cliente. Qualquer informação incorreta ou erro
    na requisição sobe essa exceção.

    Exemplos:
        - Body vazio
        - Body com campos errados
        - Valores incorretos
    """
    def __init__(self, message: str):
        super().__init__(message, type="Bad Request", status_code=400)