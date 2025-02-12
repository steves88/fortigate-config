from fortigate_api import send_request

def create_firewall_policy(policy_data):
    """ Add a new firewall policy """
    return send_request("POST", "firewall/policy", policy_data)

def get_firewall_policies():
    """ Retrieve all firewall policies """
    return send_request("GET", "firewall/policy")

def delete_firewall_policy(policy_id):
    """ Delete a specific firewall policy """
    return send_request("DELETE", f"firewall/policy/{policy_id}")
