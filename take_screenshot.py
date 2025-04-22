# take_screenshot.py

import logging
from ppadb.client import Client as AdbClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

ADB_HOST = "127.0.0.1"
ADB_PORT = 5037

def main():
    logging.info("Connecting to ADB...")
    client = AdbClient(host=ADB_HOST, port=ADB_PORT)
    devices = client.devices()

    if len(devices) == 0:
        logging.error("No device found!")
        return

    device = devices[0]
    logging.info(f"Connected to device: {device.serial}")

    screenshot_path = "/sdcard/screen_capture.png"

    # Take screenshot
    logging.info(f"Taking screenshot and saving to {screenshot_path}...")
    device.shell(f"screencap -p {screenshot_path}")

    # Pull the screenshot to computer
    logging.info("Pulling screenshot to local folder...")
    device.pull(screenshot_path, "screen_capture.png")

    logging.info("✅ Screenshot saved as 'screen_capture.png'!")

if __name__ == "__main__":
    main()
