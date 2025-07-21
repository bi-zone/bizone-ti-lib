import typing
from bizone_ti.api import manager as api_manager


ApiManagers = typing.TypeVar('ApiManagers',
                             api_manager.ApiManager,
                             api_manager.IoCApiManager)
