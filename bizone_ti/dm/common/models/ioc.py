import dataclasses


from bizone_ti.dm.common import (
    industries,
    mitre_phases,
)
from bizone_ti.dm.common import base
from bizone_ti.dm.common import types


@dataclasses.dataclass
class Reason(base.BaseDMManager):
    rule_id: str = dataclasses.field(default="")
    processor: str = dataclasses.field(default="")
    rule_name: str = dataclasses.field(default="")


@dataclasses.dataclass
class IP(base.BaseDMManager):
    ip: str

    def to_dict(self) -> str:
        return self.ip


@dataclasses.dataclass
class Port(base.BaseDMManager):
    port: str

    def to_dict(self) -> int:
        return int(self.port)


@dataclasses.dataclass
class FQDN(base.BaseDMManager):
    fqdn: str

    def to_dict(self) -> str:
        return self.fqdn


@dataclasses.dataclass
class URL(base.BaseDMManager):
    url: str

    def to_dict(self) -> str:
        return self.url


@dataclasses.dataclass
class FileName(base.BaseDMManager):
    name: str

    def to_dict(self) -> str:
        return self.name


@dataclasses.dataclass
class FeedBack(base.BaseDMManager):
    like: bool = dataclasses.field(default=False)
    dislike: bool = dataclasses.field(default=False)

    def to_dict(self) -> list[int, int]:
        return [int(self.like), int(self.dislike)]


@dataclasses.dataclass
class CommonIoCData(base.BaseDMManager):
    _: dataclasses.KW_ONLY
    tlp: str
    tti_organization: str
    user_viewed: bool
    hidden: bool
    mitre_phases: list[mitre_phases.MitrePhases]
    industry: list[industries.Industries]
    id: str
    updated: int
    threat_name: list[str]
    source: str
    description: str
    tags: list[str]
    details: dict
    category: list[str]
    ttl: int
    value: str
    removed_manually: bool
    false_positive: bool
    created: int
    services: list[str] = dataclasses.field(default_factory=lambda: [])
    last_seen: int = dataclasses.field(default=0)
    first_seen: int = dataclasses.field(default=0)
    risk_score: int = dataclasses.field(default=0)
    removed: bool = dataclasses.field(default=False)
    confidence: int = dataclasses.field(default=0)


@dataclasses.dataclass
class BaseIoC(base.BaseDMManager):
    _: dataclasses.KW_ONLY
    value: str
    entity: types.IoCTypes
    common_id: str
    state: str
    feedback: FeedBack = dataclasses.field(default_factory=lambda: [0, 0])
    files_count: int = dataclasses.field(default=0)
    severity: int = dataclasses.field(default=0)
    comment_count: int = dataclasses.field(default=0)
    linked_group_count: int = dataclasses.field(default=0)
    linked_ioc_count: int = dataclasses.field(default=0)


@dataclasses.dataclass
class IoCURLData(CommonIoCData):
    duplicate_url: str
    files: list[str]
    ips: list[IP]
    original_value: str
    protocol: str
    referer: str
    telegram_id: str
    telegram_nick: list[str]


@dataclasses.dataclass
class IoCFQDNData(CommonIoCData):
    ips: list[IP]
    original_value: str
    referer: str


@dataclasses.dataclass
class IoCIPv4Data(CommonIoCData):
    _: dataclasses.KW_ONLY
    asn: str
    fqdns: list[FQDN]
    port: list[Port]


@dataclasses.dataclass
class IoCFileData(CommonIoCData):
    extension: str
    file_name: list[FileName]
    fqdns: list[FQDN]
    ips: list[IP]
    md5: str
    path: str
    sha1: str
    sha256: str
    sha512: str
    ssdeep: str
    urls: list[URL]
    vt_score_malicious: int
    file_size: int = dataclasses.field(default=0)
    vt_score_total: int = dataclasses.field(default=0)


@dataclasses.dataclass
class IoCIPv6Data(CommonIoCData):
    _: dataclasses.KW_ONLY
    asn: str
    fqdns: list[FQDN]
    port: list[Port]
