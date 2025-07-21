import enum
import typing

from bizone_ti import exceptions
from bizone_ti.dm.common import types


class ObjectTypes(enum.Enum):
    ioc = types.IoCTypes
    group = types.GroupTypes

    @classmethod
    def objects(cls) -> tuple[enum.Enum]:
        return tuple(c.value for c in cls)

    @classmethod
    def has_value(cls, value: str) -> bool:
        return any(obj.has_value(value) for obj in cls.objects())

    @classmethod
    def get_object(cls, value: str) -> enum.Enum:
        for obj in cls.objects():
            if obj.has_value(value):
                return obj(value)
        raise exceptions.UnexpectedValueException(
                unknown_value=value,
                objs=cls)


class BaseObjectManager():
    def __init__(self, object_type: typing.Union[ObjectTypes, str]) -> None:
        if not self.__is_object_type_supported(object_type):
            raise exceptions.InvalidObjectType(
                unsupported_type=object_type,
                expected_type=[ObjectTypes, str])

        if isinstance(object_type, str):
            object_type = ObjectTypes.get_object(object_type)

        self._resource = object_type.value
        self._entity_type = object_type

    @staticmethod
    def __is_object_type_supported(object_type: typing.Union[ObjectTypes, str]
                                   ) -> bool:
        if isinstance(object_type, str):
            return ObjectTypes.has_value(object_type)
        elif isinstance(object_type, ObjectTypes.objects()):
            return True
        return False

    @property
    def resource(self) -> str:
        return self._resource

    @property
    def entity_type(self) -> typing.Union[ObjectTypes, str]:
        return self._entity_type

    def __repr__(self) -> str:
        return f'Object type <{self._entity_type}>'
