import requests

# FortiGate details
FORTIGATE_IP = "x.x.x.x"  # Replace with your FortiGate IP
API_KEY = "xxxxxxxxxxx"  # Replace with your API Key
BASE_URL = f"https://{FORTIGATE_IP}/api/v2/cmdb"

# Headers
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Sample Firewall Policy to add
firewall_policy = {
    "json": {
        "policyid": 100,  # Change policy ID if needed
        "name": "Allow Web Traffic",
        "srcintf": [{"name": "port1"}],
        "dstintf": [{"name": "port2"}],
        "srcaddr": [{"name": "all"}],
        "dstaddr": [{"name": "all"}],
        "service": [{"name": "HTTP"}, {"name": "HTTPS"}],
        "action": "accept",
        "schedule": "always",
        "logtraffic": "all",
        "status": "enable"
    }
}

# Function to create a firewall policy
def create_firewall_policy():
    url = f"{BASE_URL}/firewall/policy"
    response = requests.post(url, headers=HEADERS, json=firewall_policy["json"], verify=False)

    if response.status_code == 200:
        print("Firewall policy added successfully.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_firewall_policy()
