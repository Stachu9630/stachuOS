import os

filenames = [
    "root.py",
    "login.py",
    "config_read.py",
    "logger.py",
    "desktop.py",
    "settings.py",
    "power.py",

]

for filename in filenames:
    size_bytes = os.path.getsize(filename)

    print(f"The file '{filename}' is {size_bytes} bytes")