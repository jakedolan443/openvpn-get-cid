#!/bin/python3
import subprocess

###  place into OpenVPN server.conf file:
###     management 127.0.0.1 <port>

management_host = "127.0.0.1"
management_port = 20800

def get_client_id(client_common_name):
    status = subprocess.run("echo 'status 2' | nc -q 5 {} {}".format(management_host, management_port), shell=True, capture_output=True).stdout.decode().split("\n")
    users = {}
    for line in status:
        line = line.split(",")
        if line[0] == "CLIENT_LIST":
            users[line[1]] = line[len(line)-2]
    cid = users[client_common_name]
    return cid

print(get_client_id("common_name"))

### common_name is CN referenced in ipp.txt
### CID is used in the management interface; can be used with 
### `client-kill {CID} [MSG]` to kill a connection
