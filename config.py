import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FORTIGATE_IP = os.getenv("FORTIGATE_IP", "192.168.1.1")  # Default IP if not set
API_KEY = os.getenv("FORTIGATE_API_KEY")

BASE_URL = f"https://{FORTIGATE_IP}/api/v2/cmdb"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
