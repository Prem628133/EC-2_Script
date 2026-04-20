# Tally Server Control Script

A simple Python script to control an AWS EC2 instance (Start, Stop, and RDP connect), similar to a Windows `.py` script.

---

## 🚀 Features

* Start EC2 instance
* Stop EC2 instance
* Connect via RDP using Public DNS
* Double click on the file to start the script.

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


## 📁 Project Structure
## Use only single file --As per usecase (If u have DNS use "tally-server_with_dns.py"  && If you don't have DNS "tally-server.py")
```
tally-server   
 ├── tally-server.py   
 ├── tally-server_with_dns.py  #
 └── README.md
```
