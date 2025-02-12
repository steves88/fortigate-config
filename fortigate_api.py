import requests
from config import BASE_URL, HEADERS

def send_request(method, endpoint, data=None):
    """ Generic function to interact with the FortiGate API """
    url = f"{BASE_URL}/{endpoint}"
    
    try:
        response = requests.request(method, url, headers=HEADERS, json=data, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return None

