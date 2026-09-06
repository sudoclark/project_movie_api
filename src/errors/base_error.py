class BaseError(Exception):
    def __init__(self, message: str, type: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.type = type
        self.status_code = status_code