import typing

from bizone_ti.dm.common import types

from bizone_ti.entities import (
    GroupAdversaryEntity,
    GroupGeneralEntity,
    GroupToolEntity,
    GroupMalwareEntity,
    GroupVulnerabilityEntity,
    GroupAttackEntity,
    GROUP_TYPE_2_ENTITY_OBJECT)

from bizone_ti.entities import (
    IoCFileEntity,
    IoCFQDNEntity,
    IoCIPv6Entity,
    IoCIPv4Entity,
    IoCURLEntity,
    IoCEmailEntity,
    IOC_TYPE_2_ENTITY_OBJECT)


class GeneralEntityIoC:
    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.ipv4,
            "ipv4"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCIPv4Entity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.url,
            "url"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCURLEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.file,
            "file"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCFileEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.ipv6,
            "ipv6"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCIPv6Entity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.fqdn,
            "fqdn"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCFQDNEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.IoCTypes.email,
            "email"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> IoCEmailEntity: ...

    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Union[
            types.IoCTypes,
            str],
        raw_data: dict,
        skip_mismatched_types=False,
    ) -> typing.Union[
        IoCFQDNEntity,
        IoCIPv4Entity,
        IoCFileEntity,
        IoCIPv6Entity,
        IoCURLEntity,
        IoCEmailEntity,
        None
    ]:
        return IOC_TYPE_2_ENTITY_OBJECT[entity_type].from_dict(
            raw_data,
            skip_mismatched_types)


class GeneralEntityGroup:
    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.adversary, "adversary"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupAdversaryEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.general, "general"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupGeneralEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.malware, "malware"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupMalwareEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.tool, "tool"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupToolEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.vulnerability,
            "vulnerability"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupVulnerabilityEntity: ...

    @typing.overload
    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Literal[
            types.GroupTypes.attack,
            "attack"],
        raw_data: dict,
        skip_mismatched_types: bool = False,
    ) -> GroupAttackEntity: ...

    @classmethod
    def from_ti(  # noqa: E704
        cls,
        entity_type: typing.Union[
            types.GroupTypes, str],
        raw_data: dict,
        skip_mismatched_types=False,
    ) -> typing.Union[
        GroupAdversaryEntity,
        GroupGeneralEntity,
        GroupToolEntity,
        GroupMalwareEntity,
        GroupVulnerabilityEntity,
        GroupAttackEntity,
        None
    ]:
        return GROUP_TYPE_2_ENTITY_OBJECT[entity_type].from_dict(
            raw_data,
            skip_mismatched_types)
