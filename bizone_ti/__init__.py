from bizone_ti.api import manager as api_manager
from bizone_ti.direct_query import DirectQueryManager
from bizone_ti.entities.general import GeneralEntityIoC, GeneralEntityGroup
from bizone_ti.managers import (
    IoCManager,
    GroupManager,
    GroupEntityManager,
    IoCEntityManager)


# Setup IoCManager
IoCManager.__manager__ = api_manager.IoCApiManager()
IoCManager.__obj__ = GeneralEntityIoC

# Setup GroupManager
GroupManager.__manager__ = api_manager.ApiManager()
GroupManager.__obj__ = GeneralEntityGroup

# Setup GroupEntityManager
GroupEntityManager.__manager__ = api_manager.ApiManager()

# Setup IoCEntityManager
IoCEntityManager.__manager__ = api_manager.IoCApiManager()


__all__ = [
    "DirectQueryManager",
    "IoCManager",
    "GroupManager",
    "GroupEntityManager",
    "IoCEntityManager"
]
