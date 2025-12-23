class AppError(Exception):
    pass


class APIConnectionError(AppError):
    pass


class ResourceNotFoundError(AppError):
    pass


class DeserializationError(AppError):
    pass


class MappingError(AppError):
    pass
