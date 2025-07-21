import enum


class BaseTIEnum(enum.Enum):
    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_


class IoCTypes(BaseTIEnum):
    file = "file"
    url = "url"
    ipv4 = "ipv4"
    fqdn = "fqdn"
    subscriber = "subscriber"
    useraccount = "useraccount"
    ja3 = "ja3"
    certificate = "certificate"
    bankcard = "bankcard"
    message = "message"
    custom = "custom"
    registrykey = "registrykey"
    email = "email"
    ipv6 = "ipv6"
    device = "device"
    process = "process"


class GroupTypes(BaseTIEnum):
    attack = "attack"
    general = "general"
    tool = "tool"
    adversary = "adversary"
    incident = "incident"
    signature = "signature"
    vulnerability = "vulnerability"
    malware = "malware"
    report = "report"
    darkweb = "darkweb"
