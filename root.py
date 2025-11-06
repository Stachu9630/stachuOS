### StachuOS 4 version 2 ###
### StachuOS 4.0.0 ###



from logger import log

from colorama import Fore
log("colorama module imported")
import setup
log("setup module imported")
import os
log("os module imported")
from customtkinter import *
log("customtkinter module imported")


root1 = None
root_options_window = None


def start_root():
    global root1

    def create_version_file():
        with open("configs/STACORE/version.STACORE", "w") as f:
            f.write("4.0.0")
            log("version file created")
            f.close()

        if not root_options_window or not root_options_window.winfo_exists():
            boot_checks()
            log("boot checks func called")
        else:
            log("boot_checks skipped because root_options_window exists")

    def root_options(event=None):
        global root_options_window
        booting.withdraw()
        root_options_window = CTkToplevel()
        root_options_window.attributes("-fullscreen", True)
        root_options_window.configure(fg_color="#00739c")

        root_options_window_title = CTkLabel(root_options_window, text="StachuOS Kernal settings", font=("Arial", 50))
        root_options_window_title.pack(pady=0, padx=0, anchor="nw")

    def boot_checks():
        ## First time checks ##
        log("boot_checks_started")
        if os.path.exists("configs/NRfiles/OSconfigured.nrf"):
            log("OS configured, Continuing...")
            pass

        else:
            log("OS not configured")
            import OS_config
            log("OS config module imported")
            OS_config.start()

        ## setup complete checks ##
        if os.path.exists("configs/NRfiles/setup_complete.NR"):
            log("setup_complete.NR file found")
            import login
            log("login module imported")
            login.login_start()
            log("login screen called from login module")


        else:
            log("setup_complete.NR file not found")
            setup.start_setup()
            log("setup module called")

    root1 = CTk()
    log("root1 created")
    root1.withdraw()
    log("root1 made invisible")
    booting = CTkToplevel()
    log("booting created")
    booting.attributes("-fullscreen", True)
    log("booting made fullscreen")
    booting.configure(fg_color="#000000")

    booting.bind("<F1>", root_options)


    booting_splash = CTkLabel(booting, text="StachuOS", font=("Arial", 100))
    booting_splash.pack(pady=400)

    root1.after(1600, create_version_file)

    try:
        root1.after(1900, booting.destroy)
        log("booting destroyed func called")
    except:
        log("booting destroyed func failed to call")

    root1.mainloop()




#except FatherFigureNotFoundError

start_root()
