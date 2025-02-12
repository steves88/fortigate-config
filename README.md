# fortigate-config
Fortigate Configuration Automation - Python



Sample Policy Data
policy = {
    "policyid": 101,
    "name": "Allow SSH",
    "srcintf": [{"name": "port1"}],
    "dstintf": [{"name": "port2"}],
    "srcaddr": [{"name": "all"}],
    "dstaddr": [{"name": "all"}],
    "service": [{"name": "SSH"}],
    "action": "accept",
    "schedule": "always",
    "logtraffic": "all",
    "status": "enable"
}

create_firewall_policy(policy)
