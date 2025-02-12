from fortigate_api import send_request

def configure_interface(name, ip, subnet, status="up"):
    """ Configure a FortiGate interface """
    data = {
        "name": name,
        "ip": f"{ip} {subnet}",
        "status": status
    }
    return send_request("PUT", f"system/interface/{name}", data)

def get_interfaces():
    """ Get all interfaces """
    return send_request("GET", "system/interface")
