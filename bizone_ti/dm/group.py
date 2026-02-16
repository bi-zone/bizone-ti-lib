import dataclasses
import typing

from bizone_ti.dm.common import models


@dataclasses.dataclass
class GroupVulnerability(models.BaseGroup):
    _: dataclasses.KW_ONLY
    published: int
    modified: int
    version: str
    coa: str
    reporter: str
    references: list[str]
    vulnerability_id: str
    category: list[str]
    href: str
    cvss: dict
    score: typing.Optional[float] = None


@dataclasses.dataclass
class GroupAdversary(models.BaseGroup):
    _: dataclasses.KW_ONLY
    aliases: list[str]
    geo: list[str]
    threat_level: str
    active_since: str
    victims: list[str]
    motivation_type: list[str]
    tools: list[str]
    origin_country: list[str]
    ttps: list[models.TTPSData]


@dataclasses.dataclass
class GroupMalware(models.BaseGroup):
    _: dataclasses.KW_ONLY
    aliases: list[str]
    malware_family: str
    coa: str
    external_class: list[str]
    geo: list[str]
    features: list[str]
    mitre_phases: list[str]
    threat_level: str
    category: list[str]
    platform: list[str]
    ttps: list[models.TTPSData]


@dataclasses.dataclass
class GroupTool(models.BaseGroup):
    _: dataclasses.KW_ONLY
    registry_keys: list[str]
    primary_mitre_attack: str
    av_verdicts: dict
    powershell: str
    other_artifacts: str
    urls: list[str]
    services_drivers: list[str]
    file_masks: list[str]
    ttps: list[models.TTPSData]
    legitimacy: str
    platform: list[str] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass
class GroupGeneral(models.BaseGroup):
    _: dataclasses.KW_ONLY
    coa: str
    category: list[str]


@dataclasses.dataclass
class GroupAttack(models.BaseGroup):
    _: dataclasses.KW_ONLY
    coa: str
    external_class: list[str]
    geo: list[str]
    attacked: str
    mitre_phases: list[str]
    threat_level: str
    category: list[str]
    extended_description_exists: bool


Group_Entity_2_TIObject = {
    "vulnerability": GroupVulnerability,
    "adversary": GroupAdversary,
    "malware": GroupMalware,
    "tool": GroupTool,
    "general": GroupGeneral,
    "attack": GroupAttack,
}


class Group:
    @classmethod
    def from_ti(cls,
                raw_data: dict,
                skip_mismatched_types: bool = False
                ) -> typing.Union[
                    GroupVulnerability,
                    GroupAdversary,
                    GroupMalware,
                    GroupTool,
                    GroupGeneral,
                    GroupAttack
    ]:
        entity = raw_data["entity"]
        return Group_Entity_2_TIObject[entity].from_dict(
            raw_data,
            skip_mismatched_types)
