import tkinter as tk
from customtkinter import *
import time
import os
from logger import log
def restart():
    config.destroy()
    log("config window destroyed")
    log("func restart started")
    from root import start_root
    start_root()
    log("root restarting...")
def start():
    global config

    log("OS Config logging alive !")
    config = tk.Tk()
    log("OS Config window created")
    config.attributes("-fullscreen", True)
    log("OS Config window made fullscreen")
    config.attributes("-topmost", True)
    log("OS Config window made topmost")
    config.title("StachuOS")

    prep_msg = (tk.Label(config, text="Preparing to configure StachuOS...", fg="black", font=("Arial", 50)))
    prep_msg.pack(pady=100)
    log("OS Config window label created")
    config.after(3000, prep_msg.pack_forget)
    log("OS Config window label removed")

    task_msg = (tk.Label(config, text=" ", fg="black", font=("Arial", 30)))
    task_msg.pack(anchor="nw", pady=200)




    config.after(3400, lambda : task_msg.config(text="running task : Creating system files [type: Folder, name: configs]"))
    try:
        os.mkdir("configs")
        log("configs folder created")
    except FileExistsError:
        log("configs folder already exists")
        pass


    config.after(3700, lambda : task_msg.config(text="running task : Creating system files [type: Folder, name: configs/STACONFIG]"))
    try:
        os.mkdir("configs/STACONFIG")
        log("configs/STACONFIG folder created")
    except FileExistsError:
        log("configs/STACONFIG folder already exists")
        pass


    config.after(4000, lambda : task_msg.config(text="running task : Creating system files [type: Folder, name: configs/TFfiles]"))
    try:
        os.mkdir("configs/TFfiles")
        log("configs/TFfiles folder created")
    except FileExistsError:
        log("configs/TFfiles folder already exists")
        pass


    config.after(4500, lambda : task_msg.config(text="running task : Creating system files [type: Folder, name: configs/NRfiles]"))
    try:
        os.mkdir("configs/NRfiles")
        log("configs/NRfiles folder created")
    except FileExistsError:
        log("configs/NRfiles folder already exists")
        pass


    config.after(4900, lambda : task_msg.config(text="running task : writing system files [type: File:TF, name: configs/TFfiles/setup_value.tf] write: False"))
    if os.path.exists("configs/TFfiles/setup_value.tf"):
        log("configs/TFfiles/setup_value.tf file already exists")
        pass
    else:
        with open("configs/TFfiles/setup_value.tf", "w") as file:
            log("configs/TFfiles/setup_value.tf file created")
            file.write("False")
            log("configs/TFfiles/setup_value.tf file written")
            file.close()
            log("configs/TFfiles/setup_value.tf file closed")


    config.after(5100, lambda: task_msg.config(text="running task : Loading task"))
    log("running task : Nothing")
    config.after(5400, lambda : task_msg.config(text="running task : Enabling logger"))
    log("running task : Enabling logger")
    config.after(5600, lambda : task_msg.config(text="running task : Logger alive"))
    log("logger is alive")
    config.after(5700, lambda: task_msg.config(text="running task : Loading task"))
    log("running task : Nothing")
    config.after(6200, lambda : task_msg.config(text="running task : Creating Images [type: Image, name: account_icon.png]"))
    log("running task : Creating Images [type: Image, name: account_icon.png]")
    config.after(6350, lambda : task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_dark_blue.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_dark_blue.png]")
    config.after(6500, lambda : task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_dark_green.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_dark_green.png]")
    config.after(6500, lambda : task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_green.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_green.png]")
    config.after(6650, lambda : task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_light_blue.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_light_blue.png]")
    config.after(6800, lambda : task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_orange.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_orange.png]")
    config.after(6950, lambda: task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_pink.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_pink.png]")
    config.after(7100, lambda: task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_purple.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_purple.png]")
    config.after(7250, lambda: task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_red.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_red.png]")
    config.after(7400, lambda: task_msg.config(text="running task : Creating Images [type: Image, name:account_icon_yellow.png]"))
    log("running task : Creating Images [type: Image, name:account_icon_yellow.png]")
    config.after(7550, lambda: task_msg.config(text="running task : Creating Images [type: Image, name: ***** ]"))
    log("running task : Creating Images [type: Image, name: Private ]")
    config.after(8000, lambda : task_msg.config(text="running task : Finished"))
    log("running task : Finished")
    log("All tasks finished")
    config.after(8200, lambda : task_msg.config(text="running task : Creating system files [type: File:NRF, name: configs/STACONFIG/OSconfigured.nrf] write: True"))
    log("setting OSconfigured.nrf to True")
    if os.path.exists("configs/NRfiles/OSconfigured.nrf"):
        log("configs/NRfiles/OSconfigured.nrf file already exists")
        pass
    else:
        with open("configs/NRfiles/OSconfigured.nrf", "w") as file:
            log("configs/NRfiles/OSconfigured.nrf file created")
            file.close()
            log("configs/NRfiles/OSconfigured.nrf file closed")
    config.after(9000, lambda : task_msg.config(text="running task : restarting"))
    config.after(9200, lambda : restart())
    log("func restart called")


    config.mainloop()