from __future__ import annotations

import enum
import logging
import types
import typing

from bizone_ti import exceptions


logger = logging.getLogger(__name__)


DM_VAR = typing.TypeVar("DM_VAR", bound="BaseDMManager")


class ConverterDM:
    """Base Converter Data Model helps you to prepare
    dict to model or model to dict

    To use this class as a converter you need to implement
    in your class methods `fields` and `get_field_type`.
    """

    @classmethod
    def __convert(
        cls,
        to_type: typing.Any,
        value: typing.Any,
        skip_mismatched_types: bool = False
    ) -> typing.Any:
        if isinstance(to_type, types.GenericAlias):
            origin_type = typing.get_origin(to_type)

            if not issubclass(origin_type, list):
                raise exceptions.UnexpectedType(
                    current_type=origin_type, expected_type=list
                )
            nested_types = typing.get_args(to_type)

            if len(nested_types) > 1:
                # TODO: Should we support more than one nested types?
                raise exceptions.TooManyArgsToProcess(
                    obj=origin_type, arguments=nested_types
                )

            if not isinstance(value, (list, tuple)):
                if skip_mismatched_types:
                    value = [value]
                else:
                    raise exceptions.InvalidObjectType(
                        unsupported_type=value, expected_type=(list, tuple)
                    )

            if len(value) == 0:
                return []

            convert_to_type = nested_types[0]

            if isinstance(value, dict):
                return convert_to_type.from_dict(value, skip_mismatched_types)

            if isinstance(value[0], dict):
                return [
                    convert_to_type.from_dict(val, skip_mismatched_types)
                    for val in value
                ]

            return [convert_to_type(val) for val in value]

        elif isinstance(value, to_type):
            return value

        elif isinstance(value, dict):
            return to_type.from_dict(value)

        elif isinstance(value, (list, tuple)):
            return to_type(*value)

        return to_type(value)

    @classmethod
    def __get_converted_data_for_model(
        cls,
        obj: DM_VAR,
        raw_data: dict,
        skip_mismatched_types: bool = False
    ) -> dict:
        converted = {}
        for field_name, value in raw_data.items():
            if field_name.lower() not in obj.fields():
                logger.debug("Skip field %s for %s", field_name.lower(), cls)
                continue

            converted[field_name.lower()] = cls.__convert(
                to_type=obj.get_field_type(field_name.lower()),
                value=value,
                skip_mismatched_types=skip_mismatched_types,
            )
        return converted

    @classmethod
    def dict2model(
        cls,
        obj: DM_VAR,
        raw_data: dict,
        skip_mismatched_types: bool = False
    ) -> dict:
        return cls.__get_converted_data_for_model(
            obj, raw_data, skip_mismatched_types)

    @classmethod
    def model2dict(
        cls,
        obj: typing.Union[
            enum.Enum, dict, list, tuple, DM_VAR, bool, str, int, float, None
        ],
    ) -> typing.Any:
        if isinstance(obj, enum.Enum):
            return obj.value
        elif isinstance(obj, dict):
            return {
                field: cls.model2dict(value) for field, value in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [cls.model2dict(item) for item in obj]
        elif isinstance(obj, BaseDMManager):
            return obj.to_dict()
        elif isinstance(obj, (bool, str, int, float)) or obj is None:
            return obj

        raise exceptions.ConvertModel2DictException(unknown_type=type(obj))


class BaseDMManager:
    """Base Data Model Manager uses for extending dm dataclasses only."""

    RAW_DATA: typing.Union[str, None] = None

    @classmethod
    def fields(cls) -> typing.Sequence[str]:
        return cls.__dataclass_fields__

    @classmethod
    def get_field_type(cls,
                       field: str) -> typing.Any:
        return cls.fields()[field].type

    @classmethod
    def from_dict(
        cls,
        raw_data: dict,
        skip_mismatched_types: bool = False
    ) -> DM_VAR:
        return cls(**ConverterDM.dict2model(cls,
                                            raw_data,
                                            skip_mismatched_types))

    def to_dict(self) -> dict:
        return {
            field: ConverterDM.model2dict(getattr(self, field))
            for field in self.fields()
        }
