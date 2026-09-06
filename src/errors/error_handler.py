from .base_error import BaseError

def error_handler(exception: Exception):
    if isinstance(exception, BaseError):
        return {
            "status_code": exception.status_code,
            "data": {
                "message": exception.message,
                "type": exception.type
            }
        }

    return {
        "status_code": 500,
        "data": {
            "message": str(exception),
            "type": "Server error"
        }
    }