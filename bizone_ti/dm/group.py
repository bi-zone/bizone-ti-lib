import dataclasses
import typing

from bizone_ti.dm.common import models


@dataclasses.dataclass(kw_only=True)
class GroupVulnerability(models.BaseGroup):
    aliases: list[str] = dataclasses.field(default_factory=lambda: [])
    attack_usage: bool = False
    coa: str = ""
    cwes: list[str] = dataclasses.field(default_factory=lambda: [])
    cvss: dict = dataclasses.field(default_factory=lambda: {})
    cvss2: float | None = dataclasses.field(default=None)
    cvss3: float | None = dataclasses.field(default=None)
    cvss4: float | None = dataclasses.field(default=None)
    cvss5: float | None = dataclasses.field(default=None)
    max_cvss: float | None = dataclasses.field(default=None)
    epss: float | None = dataclasses.field(default=None)
    epss_percentile: float | None = dataclasses.field(default=None)
    has_exploits: bool = False
    cisa_kev_added: str | None = dataclasses.field(default=None)
    reporter: str = ""
    published: str = ""
    affected_products: list[models.AffectedProducts] = dataclasses.field(
        default_factory=lambda: [])
    references: list[str] = dataclasses.field(default_factory=lambda: [])
    poc_references: list[str] = dataclasses.field(default_factory=lambda: [])
    detected: str | None = dataclasses.field(default=None)
    vulnerability_id: str = ""
    has_fix: bool = False
    darkweb_usage: bool = False
    impacts: list[str] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass(kw_only=True)
class GroupAdversary(models.BaseGroup):
    aliases: list[str] = dataclasses.field(default_factory=lambda: [])
    threat_level: str = ""
    geo: list[str] = dataclasses.field(default_factory=lambda: [])
    active_since: str = ""
    victims: list[str] = dataclasses.field(default_factory=lambda: [])
    motivation_type: list[str] = dataclasses.field(default_factory=lambda: [])
    tools: list[str] = dataclasses.field(default_factory=lambda: [])
    origin_country: list[str] = dataclasses.field(default_factory=lambda: [])
    ttps: list[models.TTPSData] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass(kw_only=True)
class GroupMalware(models.BaseGroup):
    aliases: list[str] = dataclasses.field(default_factory=lambda: [])
    malware_family: str = ""
    coa: str = ""
    external_class: list[str] = dataclasses.field(default_factory=lambda: [])
    geo: list[str] = dataclasses.field(default_factory=lambda: [])
    features: list[str] = dataclasses.field(default_factory=lambda: [])
    mitre_phases: list[str] = dataclasses.field(default_factory=lambda: [])
    threat_level: str = ""
    category: list[str] = dataclasses.field(default_factory=lambda: [])
    platform: list[str] = dataclasses.field(default_factory=lambda: [])
    ttps: list[models.TTPSData] = dataclasses.field(default_factory=lambda: [])
    last_seen: str | None = dataclasses.field(default=None)
    first_seen: str | None = dataclasses.field(default=None)


@dataclasses.dataclass(kw_only=True)
class GroupTool(models.BaseGroup):
    registry_keys: list[str] = dataclasses.field(default_factory=lambda: [])
    primary_mitre_attack: str = ""
    av_verdicts: dict = dataclasses.field(default_factory=lambda: {})
    powershell: str = ""
    other_artifacts: str = ""
    urls: list[str] = dataclasses.field(default_factory=lambda: [])
    services_drivers: list[str] = dataclasses.field(default_factory=lambda: [])
    file_masks: list[str] = dataclasses.field(default_factory=lambda: [])
    ttps: list[models.TTPSData] = dataclasses.field(default_factory=lambda: [])
    legitimacy: str = ""
    platform: list[str] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass(kw_only=True)
class GroupGeneral(models.BaseGroup):
    coa: str = ""
    category: list[str] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass(kw_only=True)
class GroupAttack(models.BaseGroup):
    coa: str = ""
    external_class: list[str] = dataclasses.field(default_factory=lambda: [])
    geo: list[str] = dataclasses.field(default_factory=lambda: [])
    attacked: str = ""
    mitre_phases: list[str] = dataclasses.field(default_factory=lambda: [])
    threat_level: str = ""
    category: list[str] = dataclasses.field(default_factory=lambda: [])


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
