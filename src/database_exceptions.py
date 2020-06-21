# Custom exceptions for datbase_edit

class PathNotFound(Exception):
    pass

class csvAlreadyExists(Exception):
    pass

class csvDoesNotExist(Exception):
    pass

class UnknownError(Exception):
    pass