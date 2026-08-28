import typing


class BaseTIException(Exception):
    """Common base class for all bizone_ti lib exceptions

    Args:
        Exception (_type_): General python exception
    """

    def __init__(self, error: typing.Any) -> None:
        self.msg = f'{error}'
        super().__init__(self.msg)


class InvalidObjectType(BaseTIException):
    def __init__(self,
                 unsupported_type: typing.Any,
                 expected_type: typing.Any) -> None:
        self.msg = (f'Invalid {unsupported_type}, '
                    f'expected {expected_type}, got {type(unsupported_type)}')
        super().__init__(self.msg)


class UnexpectedType(BaseTIException):
    def __init__(self,
                 current_type: typing.Any,
                 expected_type: typing.Any) -> None:
        self.msg = (f'Got unexpected type {current_type} '
                    f' but expected {expected_type}')
        super().__init__(self.msg)


class TooManyArgsToProcess(BaseTIException):
    def __init__(self, obj: typing.Any, arguments: typing.Any) -> None:
        self.msg = (f'Object {obj} has '
                    f' to many arguments {arguments} to process')
        super().__init__(self.msg)


class ConvertModel2DictException(BaseTIException):
    def __init__(self, unknown_type: typing.Any) -> None:
        self.msg = f"Unknown type {unknown_type} to convert"
        super().__init__(self.msg)


class UnexpectedValueException(BaseTIException):
    def __init__(self, unknown_value: typing.Any, objs: typing.Any) -> None:
        self.msg = f"Unknown value {unknown_value} in {objs}"
        super().__init__(self.msg)


class InvalidAPISettings(BaseTIException):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)


class NotEnoughValues(BaseTIException):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)
