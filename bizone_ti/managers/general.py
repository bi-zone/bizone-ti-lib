from bizone_ti.managers import (
    BaseIoCEntityManager,
    BaseGroupEntityManager,
    GroupObjectsManager,
)

from bizone_ti.objects import BaseObjectManager
from bizone_ti.managers import IoCObjectsManager


class IoCEntityManager(BaseIoCEntityManager):
    """
    General manager for obtaining IoC entities from TI.
    """


class GroupEntityManager(BaseGroupEntityManager):
    """
    General manager for obtaining groups entities from TI.
    """


class BaseGroupInterface(GroupEntityManager, BaseObjectManager):
    pass


class BaseIoCInterface(IoCEntityManager, BaseObjectManager):
    pass


class IoCManager(BaseObjectManager, IoCObjectsManager):
    """
    General manager for obtaining IoCs from TI.
    """


class GroupManager(BaseObjectManager, GroupObjectsManager):
    """
    General manager for obtaining groups from TI.
    """
