__all__ = [
    'ClientConfigurationException',
    'MethodNotImplementedException',
    'EmptyApiResponseException',
    'UnexpectedApiResponseStructureException',
]


from exceptions.base_app import BaseAppException


class ClientConfigurationException(BaseAppException):
    pass


class MethodNotImplementedException(BaseAppException):
    pass


class EmptyApiResponseException(BaseAppException):
    pass


class UnexpectedApiResponseStructureException(BaseAppException):
    pass
