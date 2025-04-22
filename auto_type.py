# auto_type.py

import logging
from ppadb.client import Client as AdbClient
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

ADB_HOST = "127.0.0.1"
ADB_PORT = 5037

def main():
    logging.info("Connecting to ADB...")
    client = AdbClient(host=ADB_HOST, port=ADB_PORT)
    devices = client.devices()

    if len(devices) == 0:
        logging.error("No device found! Connect your phone.")
        return

    device = devices[0]
    logging.info(f"Connected to device: {device.serial}")

    # Type text
    message = "Hello, this is a test automation from Python! 😎"
    logging.info(f"Typing message: {message}")

    # Give you time to manually focus on an input field (e.g., in WhatsApp chat)
    logging.info("You have 5 seconds to tap on the text field...")
    time.sleep(5)

    # Input the text
    device.shell(f'input text "{message}"')

    logging.info("✅ Message typed successfully!")

if __name__ == "__main__":
    main()
