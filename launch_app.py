# launch_app.py

import logging
from ppadb.client import Client as AdbClient

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Default ADB settings
ADB_HOST = "127.0.0.1"
ADB_PORT = 5037

def main():
    logging.info("Connecting to ADB...")
    client = AdbClient(host=ADB_HOST, port=ADB_PORT)
    devices = client.devices()

    if len(devices) == 0:
        logging.error("No device found! Make sure the phone is connected.")
        return

    device = devices[0]
    logging.info(f"Connected to device: {device.serial}")

    # Replace this with your target app package name (example: WhatsApp)
    package_name = "com.whatsapp"

    # Command to launch the app
    logging.info(f"Launching app: {package_name}")
    device.shell(f"monkey -p {package_name} -c android.intent.category.LAUNCHER 1")

    logging.info("✅ App launched!")

if __name__ == "__main__":
    main()
