from bizone_ti.dm import group
from bizone_ti.dm.common import types

from bizone_ti.managers.general import BaseGroupInterface


class GroupVulnerabilityEntity(
    group.GroupVulnerability,
    BaseGroupInterface
):
    _resource = types.GroupTypes.vulnerability.value
    _entity_type = types.GroupTypes.vulnerability


class GroupAdversaryEntity(
    group.GroupAdversary,
    BaseGroupInterface
):
    _resource = types.GroupTypes.adversary.value
    _entity_type = types.GroupTypes.adversary


class GroupMalwareEntity(
    group.GroupMalware,
    BaseGroupInterface
):
    _resource = types.GroupTypes.malware.value
    _entity_type = types.GroupTypes.malware


class GroupToolEntity(
    group.GroupTool,
    BaseGroupInterface
):
    _resource = types.GroupTypes.tool.value
    _entity_type = types.GroupTypes.tool


class GroupGeneralEntity(
    group.GroupGeneral,
    BaseGroupInterface
):
    _resource = types.GroupTypes.general.value
    _entity_type = types.GroupTypes.general


GROUP_TYPE_2_ENTITY_OBJECT = {
    types.GroupTypes.adversary: GroupAdversaryEntity,
    types.GroupTypes.general: GroupGeneralEntity,
    types.GroupTypes.malware: GroupMalwareEntity,
    types.GroupTypes.tool: GroupToolEntity,
    types.GroupTypes.vulnerability: GroupVulnerabilityEntity,
    "adversary": GroupAdversaryEntity,
    "general": GroupGeneralEntity,
    "malware": GroupMalwareEntity,
    "tool": GroupToolEntity,
    "vulnerability": GroupVulnerabilityEntity,
}
