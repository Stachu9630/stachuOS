import requests
from logger import log
import os
def install_update():
    pass

def download_update():
    log("starting to download update")
    if not os.path.exists("update_files"):
        os.mkdir("update_files")






def check_updates():
    with open("configs/STACORE/version.STACORE", "r") as file:
        version = file.read()
        version.strip()
        file.close()
    VERSION_URL = "https://raw.githubusercontent.com/Stachu9630/StachuOS/main/version.txt"
    try:
        response = requests.get(VERSION_URL, timeout=5)
        if response.status_code == 200:
            available_version = response.text.strip()
            if response.text.strip == version:
                log("no update needed")
            else:
                log("update available")
                log(f"current version: {version}, available version: {available_version}")

        else:
            return None
    except Exception as e:
        log("Failed to check for updates")


