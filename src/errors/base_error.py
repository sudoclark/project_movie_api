class BaseError(Exception):
    """
    Essa é a classe modelo dos erros personalizados, ela define a estrutura que as exeções terão.

    Args:
        - message(str): Mensagem de erro explicando o motivo
        - type(str): Tipo detalhado do erro
        - status_code(int): Código de resposta daquele erro
    """
    def __init__(self, message: str, type: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.type = type
        self.status_code = status_code