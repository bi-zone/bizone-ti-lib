import dataclasses


from bizone_ti.dm.common import base
from bizone_ti.dm.common import types


@dataclasses.dataclass(kw_only=True)
class Affected(base.BaseDMManager):
    bounds: list[str] = dataclasses.field(default_factory=lambda: [])
    relation: str = ""

    def to_dict(self) -> str:
        return {
            "bounds": self.bounds,
            "relation": self.relation
        }


@dataclasses.dataclass(kw_only=True)
class AffectedProducts(base.BaseDMManager):
    vendor: str = ""
    product: str = ""
    platforms: list[str] = dataclasses.field(default_factory=lambda: [])
    affected: list[Affected] = dataclasses.field(default_factory=lambda: [])

    def to_dict(self) -> str:
        return {
            "vendor": self.vendor,
            "product": self.product,
            "platforms": self.platforms,
            "affected":
                [affected_item.to_dict() for affected_item in self.affected]
        }


@dataclasses.dataclass(kw_only=True)
class TTPSData(base.BaseDMManager):
    mitre_technique_id: str = dataclasses.field(default=None)
    procedure: str = dataclasses.field(default=None)
    command: str = dataclasses.field(default=None)


@dataclasses.dataclass(kw_only=True)
class BaseGroup(base.BaseDMManager):
    entity: types.GroupTypes
    name: str = ""
    tlp: str = ""
    industry: list[str] = dataclasses.field(
        default_factory=lambda: [])
    updated: int = 0
    date: int = 0
    created: int = 0
    source: str = ""
    state: str = ""
    tti_organization: str = ""
    description: str = ""
    comment_count: int = 0
    tags: list[str] = dataclasses.field(default_factory=lambda: [])
    files_count: int = 0
    id: str
    details: dict = dataclasses.field(default_factory=lambda: {})
    linked_group_count: int = 0
    linked_ioc_count: int = 0
    mitre_attack: list[str] = dataclasses.field(default_factory=lambda: [])
    extended_description_exists: bool = False
    services: list[str] = dataclasses.field(default_factory=lambda: [])
    hidden: bool = False
    user_viewed: bool = False
    removed_manually: bool = False
    removed: bool = False
