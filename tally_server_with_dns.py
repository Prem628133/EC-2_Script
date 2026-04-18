import boto3
import os
import subprocess
import time

# ==============================
# AWS CONFIG
# ==============================

AWS_REGION = "REGION_HERE"  # e.g.,
INSTANCE_ID = "i-xxxxxxxxxxxxxxxxx"

AWS_ACCESS_KEY = "YOUR_ACCESS_KEY_HERE"
AWS_SECRET_KEY = "YOUR_SECRET_KEY_HERE"


DNS_ADDRESS = "HARDCODED_DNS_HERE"  # Replace with your instance's public DNS if you want to hardcode it

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
# GET INSTANCE DATA
# ==============================


def get_instance():
    try:
        response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
        return response["Reservations"][0]["Instances"][0]
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_state():
    instance = get_instance()
    return instance["State"]["Name"] if instance else "unknown"

# ==============================
# ACTIONS
# ==============================


def start_instance():
    state = get_state()
    print("\nCurrent Status:", state)

    if state in ["running", "pending"]:
        print("Server already running/starting.")
        return

    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("Start request sent...")
    wait_state("running")


def stop_instance():
    state = get_state()
    print("\nCurrent Status:", state)

    if state in ["stopped", "stopping"]:
        print("Server already stopped/stopping.")
        return

    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("Stop request sent...")
    wait_state("stopped")


def wait_state(target, timeout=120):
    for _ in range(timeout):
        state = get_state()
        print("State:", state)
        if state == target:
            print("Reached:", target)
            return
        time.sleep(2)
    print("Timeout waiting for state change")

# ==============================
# RDP CONNECT (HARDCODED DNS)
# ==============================


def rdp_connect():
    state = get_state()

    if state != "running":
        print("\nERROR: Server not running.")
        return

    dns = DNS_ADDRESS

    print(f"\nConnecting to: {dns}")

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
        print("\n==============================")
        print("      TALLY SERVER CONTROL")
        print("==============================")
        print("1. Start Server")
        print("2. Stop Server")
        print("3. RDP Connect")
        print("4. Exit")

        choice = input("\nEnter option: ")

        if choice == "1":
            start_instance()
        elif choice == "2":
            stop_instance()
        elif choice == "3":
            rdp_connect()
        elif choice == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
