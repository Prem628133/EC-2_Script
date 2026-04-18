import boto3
import os
import subprocess
import time

# ==============================
# AWS CONFIG
# ==============================

AWS_REGION = "ap-south-2"
INSTANCE_ID = ""

AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""

# ==============================
# BOTO3 CLIENT
# ==============================

ec2 = boto3.client(
    "ec2",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# ==============================
# CORE LOGIC
# ==============================


def get_instance_data():
    try:
        response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
        return response["Reservations"][0]["Instances"][0]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def get_state():
    data = get_instance_data()
    return data["State"]["Name"] if data else "unknown"


def get_dns():
    data = get_instance_data()
    return data.get("PublicDnsName", "") if data else ""

# ==============================
# ACTIONS
# ==============================


def start_instance():
    state = get_state()
    if state in ["running", "pending"]:
        print("Server already running.")
        return
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("Start command sent...")
    wait_state("running")


def stop_instance():
    state = get_state()
    if state in ["stopped", "stopping"]:
        print("Server already stopped.")
        return
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("Stop command sent...")
    wait_state("stopped")


def wait_state(target, timeout=120):
    for _ in range(timeout):
        state = get_state()
        print(f"Current State: {state}")
        if state == target:
            print(f"Reached: {target}")
            return
        time.sleep(2)
    print("Timeout!")


def rdp_connect():
    state = get_state()
    if state != "running":
        print("Server is not running. Start it first.")
        return

    dns = get_dns()

    if not dns:
        print("Error: Could not find Public DNS.")
        return

    print(f"Connecting to: {dns}")

    rdp_file = os.path.join(os.getenv("TEMP", "."), "tally.rdp")

    with open(rdp_file, "w") as f:
        f.write(f"full address:s:{dns}:3389\n")
        f.write("prompt for credentials:i:1\n")
        f.write("administrative session:i:1\n")

    subprocess.run(["mstsc", rdp_file])

# ==============================
# MENU
# ==============================


def menu():
    while True:
        print("\n--- TALLY SERVER CONTROL ---")
        print("1. Start Server\n2. Stop Server\n3. RDP Connect\n4. Exit")
        choice = input("Enter option: ")
        if choice == "1":
            start_instance()
        elif choice == "2":
            stop_instance()
        elif choice == "3":
            rdp_connect()
        elif choice == "4":
            break


if __name__ == "__main__":
    menu()
