# connect_phone.py

import logging
from ppadb.client import Client as AdbClient

# -------------------
# Configure Logging
# -------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

# -------------------
# ADB Client Setup
# -------------------
# Default ADB host and port
ADB_HOST = "127.0.0.1"
ADB_PORT = 5037

def main():
    logging.info("Starting ADB client...")

    # Connect to ADB server
    client = AdbClient(host=ADB_HOST, port=ADB_PORT)

    logging.info("Searching for connected devices...")

    # Get list of connected devices
    devices = client.devices()

    if len(devices) == 0:
        logging.error("No devices found! 📱 ❌ Make sure your phone is connected via Wireless ADB.")
        return

    # Pick the first device (you can expand this later to select)
    device = devices[0]
    logging.info(f"Connected to device: {device.serial}")

    # Test connection by getting the phone's model name
    model = device.shell("getprop ro.product.model").strip()
    logging.info(f"Device Model: {model}")

    # Test connection by getting the Android version
    android_version = device.shell("getprop ro.build.version.release").strip()
    logging.info(f"Android Version: {android_version}")

    logging.info("✅ Phone is ready for automation!")

if __name__ == "__main__":
    main()
