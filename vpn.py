from fortigate_api import send_request

def create_vpn_tunnel(name, remote_gw, psk, local_net, remote_net):
    """ Creates a VPN Tunnel, defines phase1/phase2 """
    data = {
        "name": name,
        "remote-gw": remote_gw,
        "psksecret": psk,
        "phase1": {
            "proposal": "aes256-sha256",
            "dhgrp": "14"
        },
        "phase2": {
            "proposal": "aes256-sha256",
            "src_subnet": local_net,
            "dst_subnet": remote_net
        }
    }
    return send_request("POST", "vpn/ipsec/phase1-interface", data)
