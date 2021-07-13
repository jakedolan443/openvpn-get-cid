# openvpn-get-cid
Python script to get OpenVPN management interface CIDs from common-names

OpenVPN management's interface is controlled by CIDs (client IDs), which allow you to access management commands
e.g. `client-kill`

The management interface allows 2 options for killing connections between a client

`kill cn`
where cn is a common-name

or

`client-kill CID MSG`
where CID is the client ID and MSG is a message that can be delivered to a client through logs. 

This is useful for implementing bandwidth caps and other systems where a client's certificate is revoked. Key revokation is not enough, as clients still remain connected post-key exchange, and no longer exchange information - so, killing a client connection is necessary.
Supplying a message keeps things ordered and tidy, and is probably nicer on the user's end too.
This message would appear in OpenVPN config (on the client side) as:
![](https://i.imgur.com/HLWzeY0.png)

The management interface is designed for manual usage; this script allows the retrieval of CIDs which can be piped
into scripts with netcat or telnet e.g.
`echo "client-kill {}" | nc -q 5 127.0.0.1 20800`

This script is intended to be imported, e.g.
```
from get_cid import get_client_id
cid = get_client_id("common-name")
```
However, this can be used in conjunction with `sys.argv`, e.g.
```
#!/bin/python3
import subprocess
import sys

client = sys.argv[1]

def get_client_id(client_common_name):
    ...

print(get_client_id(client))
```
And called by
```
./get_cid "common-name"
```
