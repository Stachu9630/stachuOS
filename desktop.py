from customtkinter import *
from ctk_components import *
import customtkinter
from config_read import username, taskbar_colour, wallpaper_colour, desktop_look
from config_read import account_icon as _account_icon
from PIL import Image
import settings
from logger import log
from icon_loader import load_icon
log("Everything imported")

# Imagine using gitHub.it's not like im too stupid for that anyway
#14/11 guess what. im using GitHub
home = None
log("home set as None")


def desktop_ui():
    import power
    global home, notification_frame

    home = CTkToplevel()
    home.attributes("-fullscreen", True)
    home.configure(fg_color=wallpaper_colour)
    home.title("StachuOS")

    home.bind("<F1>", power.desktop_power_options)
    
    log("home window made")

     
    
    def open_start_menu():
        
        def power_btn_pressed():
            import power
            start.destroy()
            power.power_options()


        def settings_btn_pressed():
            import settings
            start.destroy()
            settings.open_settings()

        def terminal_btn_pressed():
            import terminal
            start.destroy()
            terminal.open_cmd()

        def calculator_btn_pressed():
            import calculator
            start.destroy()
            calculator.open_calculator()


        def start_menu():
            global start

            start = CTkToplevel()
            start.title("start menu")
            start.configure(width=1000)
            start.config(height=1000)
            start.attributes("-topmost", True)
            start.attributes("-toolwindow", True)

            greeting_start = CTkLabel(start, text="hello " + username, font=("Helvetica", 45))
            greeting_start.place(x=115, y=25)


            if _account_icon == "":
                account_icon = load_icon("account_icon", (96, 96))

            elif _account_icon == "red":
                account_icon = load_icon("account_icon_red", (96, 96))

            elif _account_icon == "green":
                account_icon = load_icon("account_icon_green", (96, 96))

            elif _account_icon == "yellow":
                account_icon = load_icon("account_icon_yellow", (96, 96))

            elif _account_icon == "orange":
                account_icon = load_icon("account_icon_orange", (96, 96))

            elif _account_icon == "pink":
                account_icon = load_icon("account_icon_pink", (96, 96))

            elif _account_icon == "purple":
                account_icon = load_icon("account_icon_purple", (96, 96))

            elif _account_icon == "lightblue":
                account_icon = load_icon("account_icon_light_blue", (96, 96))

            elif _account_icon == "darkblue":
                account_icon = load_icon("account_icon_dark_blue", (96, 96))

            else:
                account_icon = load_icon("account_icon", (96, 96))

            account_txt = CTkLabel(
                start,
                image=account_icon,
                text="",
                fg_color="transparent")

            account_txt.place(y=1, x=1)





            power_icon = load_icon("power_icon", (96, 96))

            power_btn = CTkButton(
                start,
                image=power_icon,
                text="",
                fg_color="transparent",
                hover_color="grey",
                width=30,
                command=power_btn_pressed)

            power_btn.place(y=890, x=1)





            settings_icon = load_icon("settings_icon", (96, 96))

            settings_btn = CTkButton(
                start,
                image=settings_icon,
                text="",
                fg_color="transparent",
                hover_color="grey",
                width=30,
                command=settings_btn_pressed)

            settings_btn.place(y=890, x=110)





            terminal_icon = load_icon("terminal_icon", (96, 96))

            terminal_btn = CTkButton(
                start,
                image=terminal_icon,
                text="",
                fg_color="transparent",
                hover_color="grey",
                width=30,
                command=terminal_btn_pressed)

            terminal_btn.place(y=890, x=220)





            calculator_icon = load_icon("calculator_icon", (96, 96))


            calculator_btn = CTkButton(
                start,
                image=calculator_icon,
                text="",
                fg_color="transparent",
                hover_color="grey",
                width=30,
                command=calculator_btn_pressed)

            calculator_btn.place(y=890, x=330)


            start.mainloop()

        start_menu()

    taskbar = CTkFrame(home,height=60, corner_radius=0, fg_color=taskbar_colour)
    taskbar.pack(side="bottom", fill="x")

    img_start_icon = load_icon("start_icon", (60, 60))
    btn_start_icon = CTkButton(home, image=img_start_icon, text="", hover_color="grey", fg_color=taskbar_colour, width=60, height=55, corner_radius=0, command=open_start_menu) #why is this image smaller than others in file explorer ##16/10 I still dont know why
    btn_start_icon.place(y=1380, x=1)    
    
    from notification_service import open_notification_frame
    notification_icon = load_icon("notification_icon", (24, 24))
    btn_notification_icon = CTkButton(home, image=notification_icon, text="", hover_color="grey", fg_color=taskbar_colour, width=60, height=55, corner_radius=0, command=open_notification_frame)
    btn_notification_icon.place(y=1383, x=2494)
    

    
    home.mainloop()


