import dataclasses


from bizone_ti.dm.common import (
    industries,
)
from bizone_ti.dm.common import base
from bizone_ti.dm.common import types


@dataclasses.dataclass
class TTPSData(base.BaseDMManager):
    _: dataclasses.KW_ONLY
    mitre_technique_id: str = dataclasses.field(default=None)
    procedure: str = dataclasses.field(default=None)
    command: str = dataclasses.field(default=None)


@dataclasses.dataclass
class BaseGroup(base.BaseDMManager):
    _: dataclasses.KW_ONLY
    entity: types.GroupTypes
    name: str
    tlp: str
    industry: list[industries.Industries]
    updated: int
    date: int
    created: int
    source: str
    state: str
    tti_organization: str
    description: str
    comment_count: int
    tags: list[str]
    files_count: int
    id: str
    details: dict
    linked_group_count: int
    linked_ioc_count: int
    mitre_attack: list[str]
    services: list[str] = dataclasses.field(default_factory=lambda: [])
    hidden: bool = dataclasses.field(default=False)
    user_viewed: bool = dataclasses.field(default=False)
    removed_manually: bool = dataclasses.field(default=False)
    removed: bool = dataclasses.field(default=False)
