from .base_error import BaseError

def error_handler(exception: Exception):
    """
    Função que trata os erros personalizados. Ela vai definir a mensagem de retorno para o usuário.

    Returns:
        - dict: Retorna todos os detalhes do erro (status code, mensagem e tipo específico)
    """
    if isinstance(exception, BaseError):
        return {
            "status_code": exception.status_code,
            "data": {
                "message": exception.message,
                "error_type": exception.error_type
            }
        }

    return {
        "status_code": 500,
        "data": {
            "message": str(exception),
            "error_type": "Server error"
        }
    }
