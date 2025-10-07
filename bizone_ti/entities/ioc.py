from bizone_ti.dm import ioc
from bizone_ti.dm.common import types

from bizone_ti.managers.general import BaseIoCInterface


class IoCFQDNEntity(ioc.IoCFQDN, BaseIoCInterface):
    _resource = types.IoCTypes.fqdn.value
    _entity_type = types.IoCTypes.fqdn


class IoCIPv4Entity(ioc.IoCIPv4, BaseIoCInterface):
    _resource = types.IoCTypes.ipv4.value
    _entity_type = types.IoCTypes.ipv4


class IoCURLEntity(ioc.IoCURL, BaseIoCInterface):
    _resource = types.IoCTypes.url.value
    _entity_type = types.IoCTypes.url


class IoCFileEntity(ioc.IoCFile, BaseIoCInterface):
    _resource = types.IoCTypes.file.value
    _entity_type = types.IoCTypes.file


class IoCIPv6Entity(ioc.IoCIPv6, BaseIoCInterface):
    _resource = types.IoCTypes.ipv6.value
    _entity_type = types.IoCTypes.ipv6


class IoCEmailEntity(ioc.IoCEmail, BaseIoCInterface):
    _resource = types.IoCTypes.email.value
    _entity_type = types.IoCTypes.email


IOC_TYPE_2_ENTITY_OBJECT = {
    types.IoCTypes.fqdn: IoCFQDNEntity,
    types.IoCTypes.ipv4: IoCIPv4Entity,
    types.IoCTypes.url: IoCURLEntity,
    types.IoCTypes.file: IoCFileEntity,
    types.IoCTypes.ipv6: IoCIPv6Entity,
    types.IoCTypes.email: IoCEmailEntity,
    "fqdn": IoCFQDNEntity,
    "ipv4": IoCIPv4Entity,
    "url": IoCURLEntity,
    "file": IoCFileEntity,
    "ipv6": IoCIPv6Entity,
    "email": IoCEmailEntity,
}
