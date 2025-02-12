import argparse
from firewall import create_firewall_policy, get_firewall_policies, delete_firewall_policy

parser = argparse.ArgumentParser(description="FortiGate Automation CLI")

parser.add_argument("--list-fw", action="store_true", help="List firewall policies")
parser.add_argument("--add-fw", type=str, help="Add a firewall policy (JSON format)")
parser.add_argument("--del-fw", type=int, help="Delete a firewall policy by ID")

args = parser.parse_args()

if args.list_fw:
    print(get_firewall_policies())
elif args.add_fw:
    import json
    policy = json.loads(args.add_fw)
    print(create_firewall_policy(policy))
elif args.del_fw:
    print(delete_firewall_policy(args.del_fw))
