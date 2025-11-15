### StachuOS 4 version 2 ###
### StachuOS 4.0.0 ###


# Make a safe mode
# rerun setup button
# reinstall stachuOS button (use update manager)
from logger import log, log_time_start, log_time_stop
import shutil
from colorama import Fore
import setup
import os
from customtkinter import *



root1 = None
root_options_window = None


def start_root():
    global root1
    def boot_checks():
        ## First time checks ##
        log("boot_checks_started")

        ## setup complete checks ##
        if os.path.exists("configs/NRfiles/setup_complete.NR"):
            log("setup_complete.NR file found")
            import login
            log("login module imported")
            log_time_stop("boot time")
            login.login_start()
            log("login screen called from login module")



        else:
            log("setup_complete.NR file not found")
            log_time_stop("boot time")
            setup.start_setup()
            log("setup module called")


    def create_module_bytecode():
        filenames = [
            "app_manager.py",
            "config_read.py",
            "desktop.py",
            "file_explorer.py",
            "icon_loader.py",
            "logger.py",
            "login.py",
            "notification_service.py",
            "power.py",
            "recovery.py",
            "root.py",
            "settings.py",
            "setup.py",
            "task_manager.py",
            "terminal.py",
            "update_manager.py"


        ]

        for filename in filenames:
            try:
                size_bytes = os.path.getsize(filename)
            except FileNotFoundError:
                log(f"ERROR: File '{filename}' not found!")
                continue

            # Log size to console
            log(f"The file '{filename}' is {size_bytes} bytes")

            # Save the size in its own file
            out_path = f"configs/STACORE/{filename}_bytecode.txt"
            with open(out_path, "w") as f:
                f.write(str(size_bytes))

        boot_checks()


    def create_version_file():
        try:
            with open("configs/STACORE/version.STACORE", "w") as f:
                f.write("4.0.0")
                log("version file created (try 1)")
                f.close()

        except FileNotFoundError:
            log("version file not found")
            try:
                os.makedirs("configs/STACORE")
                with open("configs/STACORE/version.STACORE", "w") as f:
                    f.write("4.0.0")
                    log("version file created (try 2)")
                    f.close()

            except FileNotFoundError:
                log("version file not found (try 2)")
                try:
                    os.makedirs("configs/STACORE")
                    with open("configs/STACORE/version.STACORE", "w") as f:
                        f.write("4.0.0")
                        log("version file created (try 3)")
                        f.close()

                except FileNotFoundError:
                    log("version file not found (try 3)")
                    log("Bootloop detected. Closing OS.")
                    exit()

        if not root_options_window or not root_options_window.winfo_exists():
            create_module_bytecode()
            log("Module bytecode func called")

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

        root_option_safe_mode = CTkButton(root_options_window, text="Boot Into Safe mode", font=("Arial", 50), fg_color="transparent", command=None)
        root_option_safe_mode.pack(pady=100, padx=100, anchor="nw")

        root_options_window.bind("<Escape>", lambda event: root_options_window.destroy())

        root_option_reset = CTkButton(root_options_window, text="Reset OS", font=("Arial", 50), fg_color="transparent", command=lambda : shutil.rmtree("configs"), text_color=("black", "white"))
        root_option_reset.pack(pady=100, padx=100, anchor="nw")


    root1 = CTk()
    log_time_start("boot time")
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
        root1.after(2000, booting.destroy)
        log("booting destroyed func called")
    except:
        log("booting destroyed func failed to call")

    root1.mainloop()




#except FatherFigureNotFoundError

start_root()
