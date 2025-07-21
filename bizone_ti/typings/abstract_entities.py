import typing

from bizone_ti.entities import general


GeneralEntities = typing.TypeVar('GeneralEntities',
                                 general.GeneralEntityGroup,
                                 general.GeneralEntityIoC)
