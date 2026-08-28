import dataclasses


from bizone_ti.dm.common import base
from bizone_ti.dm.common import types


@dataclasses.dataclass
class IP(base.BaseDMManager):
    ip: str = ""

    def to_dict(self) -> str:
        return self.ip


@dataclasses.dataclass
class Port(base.BaseDMManager):
    port: int = 0

    def to_dict(self) -> int:
        return int(self.port)


@dataclasses.dataclass
class FQDN(base.BaseDMManager):
    fqdn: str = ""

    def to_dict(self) -> str:
        return self.fqdn


@dataclasses.dataclass
class URL(base.BaseDMManager):
    url: str = ""

    def to_dict(self) -> str:
        return self.url


@dataclasses.dataclass
class FileName(base.BaseDMManager):
    name: str = ""

    def to_dict(self) -> str:
        return self.name


@dataclasses.dataclass(kw_only=True)
class CommonIoCData(base.BaseDMManager):
    tlp: str = ""
    tti_organization: str = ""
    user_viewed: bool = False
    hidden: bool = False
    mitre_phases: list[str] = dataclasses.field(
        default_factory=lambda: [])
    industry: list[str] = dataclasses.field(
        default_factory=lambda: [])
    id: str
    updated: int = 0
    threat_name: list[str] = dataclasses.field(default_factory=lambda: [])
    source: str
    description: str = ""
    tags: list[str] = dataclasses.field(default_factory=lambda: [])
    details: dict = dataclasses.field(default_factory=lambda: {})
    category: list[str] = dataclasses.field(default_factory=lambda: [])
    ttl: int = 0
    value: str
    removed_manually: bool = False
    false_positive: bool = False
    created: int = 0
    services: list[str] = dataclasses.field(default_factory=lambda: [])
    last_seen: int = 0
    first_seen: int = 0
    risk_score: int = 0
    removed: bool = False
    confidence: int = 0


@dataclasses.dataclass(kw_only=True)
class BaseIoC(base.BaseDMManager):
    value: str
    entity: types.IoCTypes
    common_id: str
    state: str = ""
    updated: int = 0
    feedback: list[int] = dataclasses.field(default_factory=lambda: [0, 0])
    files_count: int = 0
    severity: int = 0
    comment_count: int = 0
    linked_group_count: int = 0
    linked_ioc_count: int = 0


@dataclasses.dataclass
class IoCURLData(CommonIoCData):
    duplicate_url: str = ""
    files: list[str] = dataclasses.field(default_factory=lambda: [])
    ips: list[IP] = dataclasses.field(default_factory=lambda: [])
    original_value: str = ""
    protocol: str = ""
    referer: str = ""
    telegram_id: str = ""
    telegram_nick: list[str] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass
class IoCFQDNData(CommonIoCData):
    ips: list[IP] = dataclasses.field(default_factory=lambda: [])
    original_value: str = ""
    referer: str = ""


@dataclasses.dataclass(kw_only=True)
class IoCIPv4Data(CommonIoCData):
    asn: str = ""
    fqdns: list[FQDN] = dataclasses.field(default_factory=lambda: [])
    port: list[Port] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass
class IoCFileData(CommonIoCData):
    extension: str = ""
    file_name: list[FileName] = dataclasses.field(default_factory=lambda: [])
    fqdns: list[FQDN] = dataclasses.field(default_factory=lambda: [])
    ips: list[IP] = dataclasses.field(default_factory=lambda: [])
    md5: str = ""
    path: str = ""
    sha1: str = ""
    sha256: str = ""
    sha512: str = ""
    ssdeep: str = ""
    urls: list[URL] = dataclasses.field(default_factory=lambda: [])
    vt_score_malicious: int = 0
    file_size: int = 0
    vt_score_total: int = 0


@dataclasses.dataclass(kw_only=True)
class IoCIPv6Data(CommonIoCData):
    asn: str = ""
    fqdns: list[FQDN] = dataclasses.field(default_factory=lambda: [])
    port: list[Port] = dataclasses.field(default_factory=lambda: [])


@dataclasses.dataclass(kw_only=True)
class IoCEmailData(CommonIoCData):
    attachments: list[str] = dataclasses.field(default_factory=lambda: [])
    body: str = ""
    sender_servers: list[str] = dataclasses.field(default_factory=lambda: [])
    urls: list[URL] = dataclasses.field(default_factory=lambda: [])
    header: list[str] = dataclasses.field(default_factory=lambda: [])
