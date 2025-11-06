import os
from PIL import Image
import customtkinter as ctk
from config_read import icon_pack as _icon_pack

ICON_FOLDER = "icons/"

def get_icon_packs():
    packs = []
    for item in os.listdir(ICON_FOLDER):
        full_path = os.path.join(ICON_FOLDER, item)
        if os.path.isdir(full_path):
            packs.append(item)
    return packs

ICON_PATHS = {
    "Legacy": "icons/legacy/",
    "New": "icons/new/",
    "Flat": "icons/flat/"
}

def load_icon(name, size=(96, 96)):
    base_path = ICON_PATHS.get(_icon_pack, os.path.join(ICON_FOLDER, _icon_pack)) + "/" + name
    light_path = base_path + "_light.png"
    dark_path  = base_path + "_dark.png"

    if not os.path.exists(light_path):
        light_path = base_path + ".png"
    if not os.path.exists(dark_path):
        dark_path = base_path + ".png"

    return ctk.CTkImage(
        light_image=Image.open(light_path),
        dark_image=Image.open(dark_path),
        size=size
    )

