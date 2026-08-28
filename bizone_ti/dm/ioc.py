import dataclasses
import typing

from bizone_ti.dm.common import models


@dataclasses.dataclass
class IoCURL(models.BaseIoC):
    data: list[models.IoCURLData] = dataclasses.field(
        default_factory=lambda: [])
    original_value: str = ""


@dataclasses.dataclass
class IoCFQDN(models.BaseIoC):
    data: list[models.IoCFQDNData] = dataclasses.field(
        default_factory=lambda: [])
    original_value: str = ""


@dataclasses.dataclass
class IoCIPv4(models.BaseIoC):
    data: list[models.IoCIPv4Data] = dataclasses.field(
        default_factory=lambda: [])


@dataclasses.dataclass
class IoCFile(models.BaseIoC):
    data: list[models.IoCFileData] = dataclasses.field(
        default_factory=lambda: [])


@dataclasses.dataclass
class IoCIPv6(models.BaseIoC):
    data: list[models.IoCIPv6Data] = dataclasses.field(
        default_factory=lambda: [])


@dataclasses.dataclass
class IoCEmail(models.BaseIoC):
    data: list[models.IoCEmailData] = dataclasses.field(
        default_factory=lambda: [])


IoC_Entity_2_TIObject = {
    "url": IoCURL,
    "fqdn": IoCFQDN,
    "ipv4": IoCIPv4,
    "file": IoCFile,
    "ipv6": IoCIPv6,
    "email": IoCEmail,
}


class IoC():
    @classmethod
    def from_ti(cls, raw_data: dict, skip_mismatched_types: bool = False
                ) -> typing.Union[
                    IoCURL,
                    IoCFQDN,
                    IoCIPv4,
                    IoCFile,
                    IoCIPv6,
                    IoCEmail,
    ]:
        entity = raw_data["entity"]
        return IoC_Entity_2_TIObject[entity].from_dict(raw_data,
                                                       skip_mismatched_types)
