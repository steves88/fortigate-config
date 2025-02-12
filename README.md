# 🚀 FortiGate Automation API

## **🔧 Features**
- ✅ **Firewall Policy Management** (Add, List, Delete)
- ✅ **Network Interface Configuration**
- ✅ **VPN Tunnel Automation**
- ✅ **CLI for easy interaction**
- ✅ **Ansible & Terraform Integration**
- ✅ **Secured API Keys with .env**

---

## **📦 Installation**
### **Step 1: Clone Repository**
```sh
git clone https://github.com/steves88/fortigate-config.git
cd fortigate-automation
```

### **Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 3: Set Up Environment Variables**
1. Create a `.env` file:
```ini
FORTIGATE_IP=192.168.1.1
FORTIGATE_API_KEY=your-api-key
```

2. Add `.env` to `.gitignore`:
```ini
.env
```

---

## **🛠 CLI Usage**
### **List Firewall Policies**
```sh
python main.py --list-fw
```

### **Add a Firewall Policy**
```sh
python main.py --add-fw '{"policyid":102, "name":"Allow ICMP", "srcintf":[{"name":"port1"}], "dstintf":[{"name":"port2"}], "srcaddr":[{"name":"all"}], "dstaddr":[{"name":"all"}], "service":[{"name":"PING"}], "action":"accept", "schedule":"always", "logtraffic":"all", "status":"enable"}'
```

### **Delete a Firewall Policy**
```sh
python main.py --del-fw 102
```

---

## **⚡ Ansible Integration**
### **Install Ansible**
```sh
pip install ansible
```

### **Configure Inventory File (`ansible/inventory.ini`)**
```ini
[fortigate]
192.168.1.1 ansible_user=admin ansible_password=yourpassword ansible_network_os=fortinet.fortios
```

### **Write Playbook (`ansible/fortigate-playbook.yml`)**
```yaml
- name: Configure FortiGate Firewall
  hosts: fortigate
  gather_facts: no
  tasks:
    - name: Create a firewall policy
      fortios_firewall_policy:
        vdom: "root"
        state: "present"
        policyid: 101
        srcintf: 
          - name: "port1"
        dstintf: 
          - name: "port2"
        srcaddr: 
          - name: "all"
        dstaddr: 
          - name: "all"
        service: 
          - name: "SSH"
        action: "accept"
        schedule: "always"
        logtraffic: "all"
        status: "enable"
```

### **Run Playbook**
```sh
ansible-playbook -i ansible/inventory.ini ansible/fortigate-playbook.yml
```

---

## **🌍 Terraform Integration**
### **Install Terraform**
```sh
brew install terraform  # macOS
sudo apt-get install terraform  # Linux
```

### **Configure Terraform (`terraform/main.tf`)**
```hcl
provider "fortios" {
  hostname = var.fortigate_ip
  token    = var.api_key
}

resource "fortios_firewall_policy" "allow_ssh" {
  name      = "Allow SSH"
  policyid  = 101
  srcintf   = ["port1"]
  dstintf   = ["port2"]
  srcaddr   = ["all"]
  dstaddr   = ["all"]
  service   = ["SSH"]
  action    = "accept"
  schedule  = "always"
  logtraffic = "all"
  status    = "enable"
}
```

### **Define Variables (`terraform/variables.tf`)**
```hcl
variable "fortigate_ip" {
  default = "192.168.1.1"
}

variable "api_key" {
  default = "your-api-key"
}
```

### **Initialize & Apply**
```sh
terraform init
terraform apply
```

---

## **📌 Roadmap**
- ✅ **Current Features**: Firewall, VPN, Interfaces, Ansible, Terraform
- 🔜 **Upcoming**:
  - 🌐 Web UI Dashboard
  - 📡 FortiGate Performance Monitoring

---

## **📜 License**
MIT License © Steve Schorn


