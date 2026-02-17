# Welcome to `bizone_ti` library!

`bizone_ti` library provides the capability to work with API of the BI.ZONE Threat Intelligence Platform.


# Prerequisites

Before installing, please ensure you have the following installed:

*   Python: version 3.11 or higher


# Context
- [`IoC`](#ioc)
   - [`Get first (one) IOC`](#get-first-one-ioc)
   - [`Get multiple IOCs`](#get-multiple-iocs)
   - [`Add IOC`](#add-ioc)
   - [`Delete IOC`](#delete-ioc)
   - [`Get linked objects to IOC`](#get-linked-objects-to-ioc)
      - [`via IoCManager`](#get-linked-via-iocmanager)
      - [`via IoCEntity`](#get-linked-via-iocentity)
   - [`Link objects to IOC`](#link-objects-to-ioc)
      - [`via IoCManager`](#link-via-iocmanager)
      - [`via IoCEntity`](#link-via-iocentity)
   - [`Unlink IOC`](#unlink-ioc)
      - [`via IoCManager`](#unlink-via-iocmanager)
      - [`via IoCEntity`](#unlink-via-iocentity)
   - [`Number of IOCs types defined`](#number-of-iocs-types-defined)
   - [`Check if IOCs value and source exist`](#check-if-iocs-value-and-source-exist)
- [`Group`](#group)
   - [`Get first (one) group`](#get-first-one-group)
   - [`Get multiple groups`](#get-multiple-groups)
   - [`Add group`](#add-group)
   - [`Get linked objects to group`](#get-linked-objects-to-group)
      - [`via GroupManager`](#get-linked-via-groupmanager)
      - [`via GroupEntity`](#get-linked-via-groupentity)
   - [`Link objects to group`](#link-objects-to-group)
      - [`via GroupManager`](#link-via-groupmanager)
      - [`via GroupEntity`](#link-via-groupentity)
   - [`Unlink objects with group`](#unlink-objects-with-group)
      - [`via GroupManager`](#unlink-via-groupmanager)
      - [`via GroupEntity`](#unlink-via-groupentity)
- [`Direct Query`](#direct-query)
   - [`Get data with DQ`](#get-data-with-dq)
   - [`Get multiple data with DQ`](#get-multiple-data-with-dq)
   - [`Create data with DQ`](#create-data-with-dq)
   - [`Patch data with DQ`](#patch-data-with-dq)
   - [`Delete data with DQ`](#delete-data-with-dq)
- [`Examples of usage`](#examples-of-usage)
   - [`Get iocs with filters applied`](#get-iocs-with-filters-applied)
   - [`Get the 100 most recently added iocs type url`](#get-the-100-most-recently-added-iocs-type-url)
   - [`Get file`](#get-file)
   - [`Upload file`](#upload-file)


# IoC

## Get first (one) IOC

There are four possibilities for getting an IOC:

- via common_id;\
      **Description**: Direct search for particular IoC.\
      **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn/ti_common_id)

- via v;\
      **Description**: Search by string.\
      **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?v=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

-  via s;\
      **Description**: Search by string in several fields depends on
       the IoC type.\
      **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?s=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

    📝 Usually searching with `s` key contains multiple responses. If you need more than one response better use [`Get multiple IOCs`](#get-multiple-iocs).

-  via ss.\
      **Description**: Search by substring.\
      **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?ss=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

    📝 Usually searching with `ss` key contains multiple responses. If you need more than one response better use [`Get multiple IOCs`](#get-multiple-iocs).


``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'

# via common_id
# Most common way to search
received_ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(
   common_id='ti_common_id',
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   false_positive=False
   )

# via v
# Most common way to search
received_ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(
   v='domain.example',
   category=["Phishing"],
   sources=["some_source"],
   confidence=75,
   severity=50,
   tags=["phishing"],
   download_from=1619527873,
   download_to=1736464784,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   false_positive=False
   )

# via s
# This search key usually returns multiple responses.
# If you use 'getone', it will return first response from the TI.
received_ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(
   s='domain.example',
   category=["Phishing"],
   sources=["some_source"],
   confidence=75,
   severity=50,
   tags=["phishing"],
   download_from=1619527873,
   download_to=1736464784,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   false_positive=False
   )

# via ss
# This search key usually returns multiple responses.
# If you use 'getone', it will return first response from the TI.
received_ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(
   ss='domain.example',
   category=["Phishing"],
   sources=["some_source"],
   confidence=75,
   severity=50,
   tags=["phishing"],
   download_from=1619527873,
   download_to=1736464784,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   false_positive=False
   )
```

`received_ioc` is an instance of one of the supported IoCEntity types or NoneType.

## Get multiple IOCs

There are five possibilities for getting several IOCs:

-  via common_id;\
   **Description**: Direct search for particular IoC.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn/ti_common_id)

 - via v;\
   **Description**: Search by string.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?v=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

 - via s;\
   **Description**: Search by string in several fields depends on the IoC type.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?s=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

 - via ss.\
   **Description**: Search by substring.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/fqdn?ss=domain.example&ignore-timeout=True&q=%28%21false_positive%26%28category%3D%3D%22Phishing%22%29%26%28source%3D%3D%22some_source%22%29%26%28tags%3D%3D%22phishing%22%29%26confidence%3E%3D75%29&from=1619527873&to=1736464784&removed-filter=not-removed&sort=desc&severity=50&limit=200&other-sources=False)

 - via only filters (good for searching all IoCs that match search
     filters).

📝 See usage of common_id, v, s and ss at [`Get first (one) IOC`](#get-first-one-ioc)


``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'

received_iocs = bizone_ti.IoCManager(object_type=ioc_type).get(
   category=["Phishing"],
   sources=["some_source"],
   confidence=70,
   severity=50,
   tags=["phishing"],
   download_from=1619527873,
   download_to=1736464784,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   false_positive=False
   )
```

`received_iocs` is instance of bizone_ti.api.response.ResponseGenerator.\
Each item of `received_iocs` is an instance of one of the supported IoCEntity types.

## Add IOC

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

new_ioc_data = {
             "value": "new_domain.example",
             "services": [],
             "user_viewed": True,
             "hidden": True,
             "mitre_phases": [],
             "industry": ["Other"],
             "removed": True,
             "original_value": "new_domain.example",
             "ips": [],
             "risk_score": 0,
             "threat_name": [],
             "removed_manually": True,
             "source": "test",
             "tlp": "green",
             "tti_organization": "",
             "description": "test description",
             "tags": [],
             "confidence": 0,
             "kc_phases": [],
             "details": {},
             "category": ["Other"],
             "ttl": 0,
             "first_seen": 0,
             "last_seen": 0,
             "false_positive": True,
         }

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
response = bizone_ti.IoCManager(
   object_type=ioc_type).add(
      data=new_ioc_data,
      take_screen=True,
      return_result=True,
      rewrite=False,
      convert_2_ti_object=True)
```

`response` type is ti_response.Response.

## Delete IOC

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
status_code, response = bizone_ti.IoCManager(object_type=ioc_type).delete(
             value=new_ioc.value, source=data.source
         )
```

`status_code` type is int.\
`response` type is dict.

## Get linked objects to IOC

There are two possibilities for getting linking objects (IOCs, groups,
etc.) to an IOC:

-   via IoCManager;
-   via IoCEntity (IoCFQDNEntity, IoCIPv4Entity,IoCFileEntity,
    IoCIPv6Entity, IoCURLEntity).

### Get linked via IoCManager

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
linked_to_ioc = bizone_ti.IoCManager(object_type=ioc_type).linked(
     common_id=entity_id,
     cursor=None,
     limit=200,
     removed=False
 )
```

`linked_to_ioc` type is ti_reponse.ResponseGenerator.

📝  The parameter `removed` set to True will return
    all IOCs, including archived ones.


### Get linked via IoCEntity

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'

# ioc is an instance of one of the supported IoCEntity types.
ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(
   v='some_domain.example'
)

linked_to_ioc = ioc.linked(
     cursor=None,
     limit=200,
     removed=False
 )
```

`linked_to_ioc` type is ti_reponse.ResponseGenerator.

📝  The parameter `removed` set to True will return
    all IOCs, including archived ones.


## Link objects to IOC

There are two possibilities for linking objects (IOCs, groups, etc.) to
an IOC:

-   via IoCManager;
-   via IoCEntity (IoCFQDNEntity, IoCIPv4Entity,IoCFileEntity,
    IoCIPv6Entity, IoCURLEntity).

### Link via IoCManager

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
result = bizone_ti.IoCManager(
   object_type=ioc_type).make_link(
      common_id='ti_common_id', # common_id ioc
      object_ids=['ti_group_type:ti_group_id',
                  'ti_group_type:ti_group_id_1',
                  'ti_ioc_type:ti_common_id']) # ioc_type:common_id
```

`result` type is ti_reponse.Response.

### Link via IoCEntity

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'

# ioc is instance of IoCEntities
ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(v='some domain')

result = ioc.make_link(
      object_ids=['ti_group_type:ti_group_id',
                  'ti_group_type:ti_group_id_1',
                  'ti_ioc_type:ti_common_id']) # ioc_type:common_id
```

`result` type is ti_reponse.Response.

## Unlink IOC

There are two possibilities for unlinking objects (IOCs, groups, etc.)
from an IOC:

-   via IoCManager;
-   via IoCEntity (IoCFQDNEntity, IoCIPv4Entity,IoCFileEntity,
    IoCIPv6Entity, IoCURLEntity).

### Unlink via IoCManager

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
result = bizone_ti.IoCManager(
   object_type=ioc_type).unlink(
      common_id='ti_common_id', # common_id ioc
      object_ids=['ti_group_type:ti_group_id',
                  'ti_group_type:ti_group_id_1',
                  'ti_ioc_type:ti_common_id']) # ioc_type:common_id
```

`result` type is ti_reponse.Response.

### Unlink via IoCEntity

``` python
import bizone_ti

from bizone_ti.dm.common import types

ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'

# ioc is instance of IoCEntities
ioc = bizone_ti.IoCManager(object_type=ioc_type).getone(v='some_domain')

result = ioc.unlink(
      object_ids=['ti_group_type:ti_group_id',
                  'ti_group_type:ti_group_id_1',
                  'ti_ioc_type:ti_common_id']) # ioc_type:common_id
```

`result` type is ti_reponse.Response.

## Number of IOCs types defined

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
amount_iocs_fqdn = bizone_ti.IoCManager(object_type=ioc_type).count()
```

`amount_iocs_fqdn` type is int.

## Check if IOCs value and source exist

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

ioc_type = types.IoCTypes.fqdn # also can use str 'fqdn'
existed_iocs = bizone_ti.IoCManager(object_type=ioc_type).exist(
   sources=['test_ti_source'],
   values=['ioc_value_1', 'ioc_value_2'],
   return_absent=False,
   removed_filter="not-removed"
)
```

`existed_iocs` type is list of strings or None.

# Group

## Get first (one) group

📝 For group objects, only vulnerability, malware, tool, adversary, and general types are supported.


There are four possibilities for getting a group:

 -  via group_id;\
    **Description**: Direct search for particular group.\
    **Raw request to TI**: [Raw Request](http://gti.bi.zone/api/vulnerability/ti_group_id?ignore-timeout=True&removed-filter=not-removed&sort=asc&other-sources=True)

 -   via s;\
    **Description**: Search by string in several fields depends on the group type.\
    **Raw request to TI**: [Raw Request](http://gti.bi.zone/api/vulnerability?s=CVE-0000-00000&ignore-timeout=True&from=1619527873&to=1619627890&removed-filter=not-removed&sort=desc&q=%28%28category%3D%3D%22Phishing%22%7Ccategory%3D%3D%22Fraud%22%29%26%28tags%3D%3D%22malware%22%29%29&severity=80&sorces=test_ti_source&limit=200&other-sources=False)

    📝 Usually searching with `ss` key contains multiple responses. If you need more than one response better use [`Get multiple groups`](#get-multiple-groups).

 -  via ss.\
    **Description**: Search by substring.\
    **Raw request to TI**: [Raw Request](http://gti.bi.zone/api/vulnerability?ss=CVE-0000-00000&ignore-timeout=True&from=1619527873&to=1619627890&removed-filter=not-removed&sort=desc&q=%28%28category%3D%3D%22Phishing%22%7Ccategory%3D%3D%22Fraud%22%29%26%28tags%3D%3D%22malware%22%29%29&severity=80&sorces=test_ti_source&limit=200&other-sources=False)

    📝 Usually searching with `ss` key contains multiple responses. If you need more than one response better use [`Get multiple groups`](#get-multiple-groups).

    📝 You can use the `motivation` parameter to search exclusively for group type `adversary`.

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'vulnerability')
group_type = types.GroupTypes.vulnerability

# via group_id
# Most common way to search
received_group = bizone_ti.GroupManager(object_type=group_type).getone(
   group_id='ti_group_id',  # group id vulnerability:ti_group_id
   ignore_timeout=True,
   removed_filter='not-removed',
   sort='asc',
   other_sources=True
)

# via s
# This search key usually returns multiple responses.
# If you use 'getone', it will return first response from the TI.
received_group = bizone_ti.GroupManager(object_type=group_type).getone(
   s='CVE-0000-00000',
   category=["Phishing", "Fraud"],
   sources=["test_ti_source"],
   severity=80,
   tags=["malware"],
   industry=["Other"],
   download_from=1619527873,
   download_to=1619627890,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
)

# via ss
# This search key usually returns multiple responses.
# If you use 'getone', it will return first response from the TI.
received_group = bizone_ti.GroupManager(object_type=group_type).getone(
   ss='CVE-0000-00000',
   category=["Phishing", "Fraud"],
   sources=["test_ti_source"],
   severity=80,
   tags=["malware"],
   industry=["Other"],
   download_from=1619527873,
   download_to=1619627890,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
)
```

`received_group` is an instance of one of the supported
GroupEntity types or NoneType.

## Get multiple groups

📝 For group objects supports only vulnerability, malware, tool, adversary,
general types.

There are five possibilities for getting several groups:

 - via group_id;\
   **Description**: Direct search for particular group.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/vulnerability/ti_group_id?ignore-timeout=True&removed-filter=not-removed&sort=asc&other-sources=True)

   📝 Searching with `group_id` key contains one response. Better use [`Get first (one) group`](#get-first-one-group).

 - via s;\
   **Description**: Search by string in several fields depends on the group type.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/vulnerability?s=CVE-0000-00000&ignore-timeout=True&from=1619527873&to=1619627890&removed-filter=not-removed&sort=desc&q=%28%28category%3D%3D%22Phishing%22%7Ccategory%3D%3D%22Fraud%22%29%26%28tags%3D%3D%22malware%22%29%29&severity=80&sorces=test_ti_source&limit=200&other-sources=False)

 - via ss.\
   **Description**: Search by substring.\
   **Raw request to TI**: [Example](http://gti.bi.zone/api/vulnerability?ss=CVE-0000-00000&ignore-timeout=True&from=1619527873&to=1619627890&removed-filter=not-removed&sort=desc&q=%28%28category%3D%3D%22Phishing%22%7Ccategory%3D%3D%22Fraud%22%29%26%28tags%3D%3D%22malware%22%29%29&severity=80&sorces=test_ti_source&limit=200&other-sources=False)

 -   via only filters (good for searching all groups that match search filters).

📝 See usage of group_id, s and ss at [`Get first (one) group`](#get-first-one-group).

📝 You can use the `motivation` parameter to search exclusively for group type `adversary`.

``` python
import bizone_ti

from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http sessiononly filters
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

 # group_type can also be str (expl: group_type = 'adversary')
group_type = types.GroupTypes.adversary

# Search only with filters 
# You can use the `motivation` parameter to search exclusively for group type `adversary`.
received_groups = bizone_ti.GroupManager(object_type=group_type).get(
   sources=["test"],
   tags=["Other"],
   motivation=["cybercriminals"],
   industry=["Other"],
   download_from=1519527873,
   download_to=1619627890,
   limit=200,
   cursor=None,
   sort='desc',
   removed_filter='not-removed',
   ignore_timeout=True,
   other_sources=False,
   )
```

`received_groups` is instance of bizone_ti.api.response.ResponseGenerator.

## Add group

📝 For group objects supports only vulnerability, malware, tool, adversary,
general types.


``` python
import uuid

import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

 # group_type can also be str (expl: group_type = 'adversary')
group_type = types.GroupTypes.adversary

new_adversary_group = {
     "aliases": [],
     "services": [],
     "name": str(uuid.uuid4()),
     "user_viewed": False,
     "geo": [],
     "threat_level": "",
     "removed": True,
     "date": 0,
     "details": {},
     "removed_manually": False,
     "mitre_attack": [],
     "source": "test",
     "active_since": "",
     "tlp": "green",
     "victims": [],
     "motivation_type": [],
     "state": "new",
     "description": "test description",
     "tags": [],
     "hidden": True,
     "tools": [],
     "industry": ["Other"],
     "origin_country": [],
     "ttps": [],
 }

response = bizone_ti.GroupManager(object_type=group_type).add(
   data=new_adversary_group,
   convert_2_ti_object=True,
)
```

`response` is instance of ti_response.Response.

## Get linked objects to group

📝 For group objects supports only vulnerability, malware, tool, adversary,
general types.

There are two possibilities for getting linked objects (IOCs, groups,
etc.) from a group

-  via GroupManager;

-  via GroupEntity (GroupAdversaryEntity, GroupGeneralEntity, GroupToolEntity, GroupMalwareEntity, GroupVulnerabilityEntity).

### Get linked via GroupManager

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

response = bizone_ti.GroupManager(object_type=group_type).linked(
   group_id='ti_group_id',  # group.id is tool:ti_group_id
     cursor='',
     limit=100,
     removed=False,
)
```

`response` is instance of ti_reponse.ResponseGenerator.

📝  The parameter `removed` set to True will return
    all IOCs, including archived ones.


### Get linked via GroupEntity

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

# The group is an instance of one of the supported GroupEntity types.
group = bizone_ti.GroupManager(object_type=group_type).getone(
   group_id='ti_group_id' # group id is tool:ti_group_id
)
response = group.linked(
   cursor='',
   limit=100,
   removed=False,
)
```

`response` is instance of ti_reponse.ResponseGenerator.

📝  The parameter `removed` set to True will return
    all IOCs, including archived ones.


## Link objects to group

📝 For group objects supports only vulnerability, malware, tool, adversary,
general types.

There are two possibilities for linking objects (IOCs, groups, etc.) to
a group

-  via GroupManager;

-  via GroupEntity (GroupAdversaryEntity, GroupGeneralEntity, GroupToolEntity, GroupMalwareEntity, GroupVulnerabilityEntity).

### Link via GroupManager

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

response = bizone_ti.GroupManager(object_type=group_type).make_link(
   group_id='ti_group_id',  # group.id is tool:ti_group_id
   object_ids=["ioc_type:ti_common_id", "ioc_type:ti_common_id_1"]
)
```

`response` is instance of ti_reponse.Response.

### Link via GroupEntity

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

# The group is an instance of one of the supported GroupEntity types.
group = bizone_ti.GroupManager(object_type=group_type).getone(
   group_id='ti_group_id')  # group.id is tool:ti_group_id

response = group.make_link(
   object_ids=["ioc_type:ti_common_id", "ioc_type:ti_common_id_1"]
)
```

`response` is instance of ti_reponse.Response.

## Unlink objects with group

📝 For group objects supports only vulnerability, malware, tool, adversary,
general types.

There are two possibilities for unlinking objects (IOCs, groups, etc.):
from a group

-  via GroupManager;

-  via GroupEntity (GroupAdversaryEntity, GroupGeneralEntity, GroupToolEntity, GroupMalwareEntity, GroupVulnerabilityEntity).

### Unlink via GroupManager

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

response = bizone_ti.GroupManager(object_type=group_type).unlink(
   group_id='ti_group_id',  # group.id is tool:ti_group_id
   object_ids=["ioc_type:ti_common_id", "ioc_type:ti_common_id_1"]
)
```

`response` is instance of ti_reponse.Response.

### Unlink via GroupEntity

``` python
import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

# group_type can also be str (expl: group_type = 'tool')
group_type = types.GroupTypes.tool

# The group is an instance of one of the supported GroupEntity types.
group = bizone_ti.GroupManager(object_type=group_type).getone(
   group_id='ti_group_id')  # group.id is tool:ti_group_id

response = group.unlink(
   object_ids=["ioc_type:ti_common_id",
               "ioc_type:ti_common_id_1"]
)
```

`response` is instance of ti_reponse.Response.


# Direct Query

Direct Query (DQ) provides a HTTP interface for creating requests to the
TI platform, including GET, POST, PATCH, PUT, and DELETE methods. Using
DQ, you can construct any request to the TI platform as desired, but you
won't receive object representations of the TI platform objects.

📝 Before using DQ, you need to set it up. For this purpose, you can use
either bizone_ti.setup.DirectQueryConfig or bizone_ti.setup.TILibConfig.
Warning: the configuration set with bizone_ti.setup.DirectQueryConfig
will take priority over bizone_ti.setup.TILibConfig.


An examples how to use the Direct Query:

## Get data with DQ

``` python
import bizone_ti
from bizone_ti import setup
from bizone_ti.dm.common import types


ioc_type = types.IoCTypes.url
common_id = "ti_common_id"

# Setup ti_url and api_key
ti_url = ''
api_key = ''

# setup api url and api key with DirectQueryConfig or TILibConfig
bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)
dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.get(
      uri='/'.join([
            ti_url,
            ioc_type.value,
            common_id]
      ),
      headers=None,
      params=None,
   )
```

`dq_response` variable type is dict.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.

## Get multiple data with DQ

``` python
import bizone_ti

from bizone_ti.api import response
from bizone_ti.dm.common import types


ioc_type = types.IoCTypes.url
params_for_dq_request = {
      "q": '(!false_positive&(source=="some_ti_source"))',
      "ignore-timeout": True,
      "removed-filter": "not-removed",
      "sort": "asc",
      "other_sources": False,
      "limit": 10,
   }

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)
dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.get(
      uri='/'.join([
            ti_url,
            ioc_type.value]
      ),
      headers=None,
      params=params_for_dq_request
   )
```

`dq_response` variable type is dict.\
The `dq_response` variable contains the raw response from the TI platform.

## Create data with DQ

``` python
import bizone_ti
from bizone_ti.api import response
from bizone_ti.dm.common import types


ioc_type = types.IoCTypes.url
new_ioc = {
               "value": "http://url.url",
               "services": [],
               "user_viewed": True,
               "hidden": True,
               "mitre_phases": [],
               "industry": ["Other"],
               "removed": True,
               "original_value": "http://url.url.test",
               "ips": [],
               "risk_score": 0,
               "threat_name": [],
               "source": "test",
               "tlp": "green",
               "tti_organization": "",
               "description": "test description",
               "tags": ["test"],
               "confidence": 0,
               "kc_phases": [],
               "details": {},
               "category": ["Other"],
               "ttl": 0,
               "first_seen": 0,
               "last_seen": 0,
               "false_positive": True,
            }

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)

dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.post(
         uri='/'.join([
               ti_url,
               ioc_type.value,
               'add']),
         headers=None,
         params=None,
         json=[new_ioc])
```

`dq_response` variable type is dict.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.

## Patch data with DQ

``` python
import bizone_ti

from bizone_ti.api import response
from bizone_ti.dm.common import types


group_type = types.GroupTypes.vulnerability
group_id = "ti_group_id"

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)

dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.patch(
      uri='/'.join([ti_url, group_type.value, group_id]),
      params=None,
      headers=None,
      json={
            "description": "new test description."
      }
   )
```

`dq_response` variable type is dict.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.

## Delete data with DQ

``` python
import bizone_ti

from bizone_ti.api import response
from bizone_ti.dm.common import types


group_type = types.GroupTypes.vulnerability
group_id = "ti_group_id"

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)

dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.delete(
               uri='/'.join([ti_url, group_type.value, group_id]),
               params=None,
               headers=None,
               json=None
            )
```

`dq_response` variable type is str.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.


# Examples of usage

A short examples of how to use the library.

## Get iocs with filters applied

``` 
import logging

import bizone_ti
from bizone_ti.dm.common import types

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formatter = logging.Formatter(
     '%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)

IOC_TYPE_2_MANAGER_MAP = {
   'file': bizone_ti.IoCManager(object_type='file'),
   'url': bizone_ti.IoCManager(object_type='url'),
   'ipv4': bizone_ti.IoCManager(object_type='ipv4'),
   'fqdn': bizone_ti.IoCManager(object_type='fqdn')
}

filters = {
   "download_from": 5000,
   "sources": [
      "test_ti_source",
      ]
}

for ioc_type, ioc_manager in IOC_TYPE_2_MANAGER_MAP.items():
   try:
      logger.info('Start download iocs type %s', ioc_type)
      iocs_generator = ioc_manager.get(
               **filters
            )

      for ioc in iocs_generator:
         logger.info('Find ioc %s', ioc.value)
   except Exception as e:
      logger.warning('HTTP error %s. Continue with next ioc_type', str(e))
```

## Get the 100 most recently added iocs type url

``` 
import itertools

import bizone_ti
from bizone_ti.dm.common import types


ti_url = '' # ti url
api_key = '' # your api key

# setup http session
bizone_ti.setup.TIHTTPSessionConfig.setup(
      http_proxy='', # set necessary http proxy
      https_proxy='' # set necessary https proxy
   )

# setup lib
bizone_ti.setup.TILibConfig.setup(ti_url=ti_url, api_key=api_key)


received_iocs = bizone_ti.IoCManager(object_type='url').get(sort='desc')

received_iocs.setup(pages_per_download=1)

top_iocs = list(itertools.islice(received_iocs, 100))
```

## Get file

``` 
import bizone_ti

from bizone_ti.api import response
from bizone_ti.dm.common import types


group_type = types.GroupTypes.vulnerability
group_id = "ti_group_id"

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)

dq = bizone_ti.DirectQueryManager()

status_code, dq_response = dq.get(
     '/'.join([ti_url, group_type.value, group_id, 'files']),
 )
```

`dq_response` variable type is list.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.

## Upload file

``` 
import bizone_ti

from bizone_ti.api import response
from bizone_ti.dm.common import types


group_type = types.GroupTypes.adversary
group_id = "ti_group_id"
bytes_str = b'some_binary_data'

# Setup ti_url and api_key
ti_url = ''
api_key = ''

bizone_ti.setup.DirectQueryConfig.setup(ti_url=ti_url, api_key=api_key)

dq = bizone_ti.DirectQueryManager()

status_code, dq_response_upload = dq.post(
   uri='/'.join(
      [ti_url, 'files', 'upload']),
   json={
      "entities":
         [
            {"entity":"ti_group_type",
            "id":"ti_group_id"}
         ],
      "metadata":
         {"file_name":"file_name.txt",
         "content_type":"text/plain",
         "description": "some description"}
   }
 )

status_code, dq_response = dq.post(
   uri=dq_response_upload["upload_url"],
   json=bytes_str
)
```

`dq_response_upload` variable type is dict.\
The `dq_response_upload` variable contains the raw response from the TI platform.
`dq_response` variable type is empty.\
The `dq_response` variable contains the raw response from the TI platform.\
`status_code` variable type is int.
