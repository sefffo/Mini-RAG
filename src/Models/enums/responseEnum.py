from enum import Enum

class ResponseSignal(Enum):
    SUCCESS = "success"
    ERROR = "error"
    FILE_TYPE_NOT_ALLOWED = "file_type_not_allowed"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_VALIDATION_FAILED = "file_validation_failed"