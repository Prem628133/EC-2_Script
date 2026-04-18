# Tally Server Control Script

A simple Python script to control an AWS EC2 instance (Start, Stop, and RDP connect), similar to a Windows `.bat` script.

---

## 🚀 Features

* Start EC2 instance
* Stop EC2 instance
* Connect via RDP using Public DNS
* Simple CLI menu (same as `.bat` version)

---

## 📦 Requirements

* Python **3.14.4**
* `boto3` (AWS SDK for Python)

---

## 🔧 Installation

### 1. Install Python

Make sure Python **3.14.4** is installed:

```bash
python3 --version
```

---

### 2. Install dependency

```bash
pip install boto3
```

---

## 🔐 AWS Configuration

Configure your AWS credentials:

```bash
aws configure
```

Provide:

* AWS Access Key
* AWS Secret Key
* Region (e.g., `ap-south-1`)

---

## ⚙️ Setup

Open the script file and update:

```python
REGION = "your-region"
INSTANCE_ID = "your-ec2-instance-id"
```

---

## ▶️ Run the Script

```bash
python3 tally-server.py
```

---

## 🖥️ Menu Options

```
1. Start Tally Server
2. Stop Tally Server
3. RDP Connect
4. Exit
```

---

## 🧠 Notes

* RDP works only when the EC2 instance is in **running** state
* Public DNS must be available
* For Linux users, install RDP client:

```bash
sudo apt install freerdp2-x11
```

---

## ⚠️ Security

* Do **NOT** hardcode AWS credentials in the script
* Use `aws configure` or IAM roles

---

## 📁 Project Structure

```
tally-server/
 ├── tally-server.py
 ├── tally-server.bat
 └── README.md
```

---

## ✅ Future Improvements

* Add RDS support
* Convert into CLI tool
* Add web interface

---
