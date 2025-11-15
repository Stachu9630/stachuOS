import urllib

import customtkinter as ctk
from ctk_components import *
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from config_read import username, password
from config_read import icon_pack as current_icon_pack
from notification_service import add_notification
from icon_loader import load_icon, get_icon_packs
from update_manager import check_updates



def back_settings_account():
    account_settings.destroy()
    settings.deiconify()

def back_settings_personalization():
    personalization_settings.destroy()
    settings.deiconify()

def back_settings_apps():
    pass

def back_settings_system():
    system_settings.destroy()
    settings.deiconify()

def back_settings_about():
    about_settings.destroy()
    settings.deiconify()

def back_settings_developer():
    developer_settings.destroy()
    settings.deiconify()



def settings_account():
    
    def change_username_open_window():

        def change_username():
            from desktop import home
            with open ("configs/STACONFIG/username.staconfig", "w") as file:
                file.write(change_username_entry.get())
                file.close()
                CTkMessagebox(title="Stax", message="Username changed successfully", icon="check", option_1="Ok")
                add_notification("Username changed successfully", "Please restart to apply changes")
                CTkNotification(home, state="info", message="Please restart to apply changes", side="right_bottom")
        change_username_window = CTkToplevel()
        change_username_window.geometry("300x200")
        change_username_window.title("Stax")
        change_username_window.attributes("-topmost", True)

        change_username_entry = CTkEntry(change_username_window, placeholder_text="Enter new username")
        change_username_entry.pack(pady=20)

        change_username_btn = CTkButton(change_username_window, text="Change", command=change_username)
        change_username_btn.pack(pady=20)

    def change_password_open_window():
        def change_password():
            from desktop import home
            with open ("configs/STACONFIG/Password.staconfig", "w") as file:
                file.write(change_password_entry.get())
                file.close()
                CTkMessagebox(title="Stax", message="Username changed successfully", icon="check", option_1="Ok")
                add_notification("Password changed successfully", "Please restart to apply changes")
                CTkNotification(home, state="info", message="Please restart to apply changes", side="right_bottom")

        def check_password():
            if current_password_entry.get() == password:
                if retype_password_entry.get() == change_password_entry.get():
                    change_password()
                else:
                    CTkMessagebox(title="Stax", message="Passwords do not match", icon="warning", option_1="Ok")
            else:
                CTkMessagebox(title="Stax", message="Wrong password", icon="warning", option_1="Ok")


        change_password_window = CTkToplevel()
        change_password_window.geometry("300x350")
        change_password_window.title("Stax")
        change_password_window.attributes("-topmost", True)

        current_password_entry = CTkEntry(change_password_window, placeholder_text="Enter current password")
        current_password_entry.pack(pady=20)

        change_password_entry = CTkEntry(change_password_window, placeholder_text="Enter new password")
        change_password_entry.pack(pady=20)

        retype_password_entry = CTkEntry(change_password_window, placeholder_text="Retype new password")
        retype_password_entry.pack(pady=20)

        change_username_btn = CTkButton(change_password_window, text="Change", command=check_password)
        change_username_btn.pack(pady=20)

    def login_pswd_require_change():
        with open("configs/STACONFIG/login_screen.staconfig", "w") as file:
            file.write(login_pswd_require_var.get())

    def shell_pswd_require_change():
        with open("configs/STACONFIG/login_screen.staconfig", "w") as file:
            file.write(login_pswd_require_var.get())

    global account_settings
    settings.withdraw()
    account_settings = ctk.CTkToplevel()
    account_settings.geometry("1000x1000")
    account_settings.title("account settings")
    account_settings.attributes("-topmost", True)

    back_icon = load_icon ("back_arrow_icon", size=(60, 60))
    back_btn = ctk.CTkButton(account_settings, image=back_icon, text="", fg_color="transparent", hover_color="grey", command=back_settings_account)
    back_btn.place(y=5, x=5)
    
    current_username_txt = CTkLabel(account_settings, text="Username : " + username, font=("Helvetica", 30))
    current_username_txt.place(x=5, y=100)

    change_username_btn = CTkButton(account_settings, text="Change", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=change_username_open_window)
    change_username_btn.place(x=5, y=150)



    current_password_txt = CTkLabel(account_settings, text="Password : " + password, font=("Helvetica", 30))
    current_password_txt.place(x=5, y=250)
    
    change_password_btn = CTkButton(account_settings, text="Change", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=change_password_open_window)
    change_password_btn.place(x=5, y=300)

    login_pswd_require_var = StringVar(value=open("configs/STACONFIG/login_screen.staconfig").read())
    login_require_pswd_txt = CTkCheckBox(account_settings, text="require password when logging in", onvalue="True", offvalue="False", variable=login_pswd_require_var, command=login_pswd_require_change , font=("Helvetica", 20))
    login_require_pswd_txt.place(x=5, y=400)

    shell_pswd_require_var = StringVar(value=open("configs/STACONFIG/shell_password_require.staconfig").read())
    shell_require_pswd_txt = CTkCheckBox(account_settings, text="require password when opening terminal", onvalue="True", offvalue="False", variable=shell_pswd_require_var, command=shell_pswd_require_change, font=("Helvetica", 20))
    shell_require_pswd_txt.place(x=5, y=450)

def settings_personalization():

    def set_defualt_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("default")
            file.close()

    def set_red_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("red")
            file.close()

    def set_lightblue_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("lightblue")
            file.close()

    def set_darkblue_icon():
            with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
                file.write("darkblue")
                file.close()

    def set_green_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("green")
            file.close()

    def set_yellow_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("yellow")
            file.close()

    def set_orange_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("orange")
            file.close()

    def set_pink_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("pink")
            file.close()

    def set_purple_icon():
        with open("configs/STACONFIG/account_icon.staconfig", "w") as file:
            file.write("purple")
            file.close()

    def icon_pack_change(new_value):
        with open("configs/STACONFIG/icon_pack.staconfig", "w") as file:
            file.write(new_value)
            CTkNotification(personalization_settings, state="info", message="Restart required to apply icon pack", side="right_bottom")
            add_notification("Icon pack changed", "Restart required to apply icon pack")

    global personalization_settings, account_red_icon
    settings.withdraw()
    personalization_settings = ctk.CTkToplevel()
    personalization_settings.geometry("1000x1000")
    personalization_settings.title("personalization settings")
    personalization_settings.attributes("-topmost", True)

    back_icon = load_icon("back_arrow_icon", size=(60, 60))
    back_btn = ctk.CTkButton(personalization_settings, image=back_icon, text="", fg_color="transparent", hover_color="grey", command=back_settings_personalization)
    back_btn.place(y=5, x=5)

    account_icon_txt = ctk.CTkLabel(personalization_settings, text="Account icons", font=("Helvetica", 40))
    account_icon_txt.place(x=0, y=100)





    account_default_icon = load_icon("account_icon", size=(80, 80))
    account_default_btn = ctk.CTkButton(
        personalization_settings,
        image=account_default_icon,
        text="", fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_defualt_icon)
    account_default_btn.place(x=0, y=150)



    account_red_icon = load_icon("account_icon_red", size=(80, 80))
    account_red_btn = ctk.CTkButton(
        personalization_settings,
        image=account_red_icon, text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_red_icon
    )
    account_red_btn.place(x=150, y=150)





    account_lightblue_icon = load_icon("account_icon_light_blue", size=(80, 80))
    account_lightblue_btn = ctk.CTkButton(
        personalization_settings,
        image=account_lightblue_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_lightblue_icon)
    account_lightblue_btn.place(x=300, y=150)



    account_darkblue_icon = load_icon("account_icon_dark_blue", size=(80, 80))
    account_darkblue_btn = ctk.CTkButton(
        personalization_settings,
        image=account_darkblue_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_darkblue_icon)
    account_darkblue_btn.place(x=450, y=150)



    account_green_icon = load_icon("account_icon_green", size=(80, 80))
    account_green_btn = ctk.CTkButton(
        personalization_settings,
        image=account_green_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_green_icon
    )
    account_green_btn.place(x=600, y=150)



    account_yellow_icon = load_icon("account_icon_yellow", size=(80, 80))
    account_yellow_btn = ctk.CTkButton(
        personalization_settings,
        image=account_yellow_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_yellow_icon
    )
    account_yellow_btn.place(x=750, y=150)



    account_orange_icon = load_icon("account_icon_orange", size=(80, 80))
    account_orange_btn = ctk.CTkButton(
        personalization_settings,
        image=account_orange_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_orange_icon
    )
    account_orange_btn.place(x=0, y=300)



    account_pink_icon = load_icon("account_icon_pink", size=(80, 80))
    account_pink_btn = ctk.CTkButton(
        personalization_settings,
        image=account_pink_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_pink_icon
    )
    account_pink_btn.place(x=150, y=300)



    account_purple_icon = load_icon("account_icon_purple", size=(80, 80))
    account_purple_btn = ctk.CTkButton(
        personalization_settings,
        image=account_purple_icon,
        text="",
        fg_color="transparent",
        hover_color="grey",
        border_width=3,
        border_color=("black", "white"),
        corner_radius=9,
        command=set_purple_icon
    )
    account_purple_btn.place(x=300, y=300)


    icon_pack_txt = ctk.CTkLabel(personalization_settings, text="Icon Packs", font=("Helvetica", 40))
    icon_pack_txt.place(x=5, y=450)

    icon_pack_var = StringVar(value=current_icon_pack)

    icon_packs = get_icon_packs()
    icon_pack_dropdown = ctk.CTkOptionMenu(
        personalization_settings,
        values=icon_packs,
        variable=icon_pack_var,
        command=icon_pack_change
    )
    icon_pack_dropdown.place(x=5, y=500)

    icon_pack_warn = CTkLabel(personalization_settings, text="Restart is required to show the Selected Icons", font=("Helvetica", 20))
    icon_pack_warn.place(x=150, y=500)

    desktop_look_txt = ctk.CTkLabel(personalization_settings, text="Desktop look", font=("Helvetica", 40))
    desktop_look_txt.place(x=5, y=650)

    desktop_look_dropdown = CTkOptionMenu(personalization_settings, values=["New", "Old", "Legacy"])
    desktop_look_dropdown.place(x=5, y=700)

    desktop_look_warn = CTkLabel(personalization_settings, text="Restart is required to show the selected desktop UI", font=("Helvetica", 20))
    desktop_look_warn.place(x=150, y=700)

def settings_apps():
    pass

def settings_system():

    global system_settings
    settings.withdraw()
    system_settings = ctk.CTkToplevel()
    system_settings.geometry("1000x1000")
    system_settings.title("System settings")
    system_settings.attributes("-topmost", True)

    back_icon = load_icon("back_arrow_icon", size=(60, 60))
    back_btn = ctk.CTkButton(system_settings, image=back_icon, text="", fg_color="transparent", hover_color="grey", command=back_settings_system)
    back_btn.place(y=5, x=5)

    check_update_btn = CTkButton(system_settings, text="Change", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=check_updates)
    check_update_btn.place(x=5, y=150)



def settings_about():
    global about_settings
    settings.withdraw()
    about_settings = ctk.CTkToplevel()
    about_settings.geometry("1000x1000")
    about_settings.title("About settings")
    about_settings.attributes("-topmost", True)

    back_icon = load_icon("back_arrow_icon", size=(60, 60))
    back_btn = ctk.CTkButton(about_settings, image=back_icon, text="", fg_color="transparent", hover_color="grey", command=back_settings_about)
    back_btn.place(y=5, x=5)

    spacing_txt = CTkLabel(about_settings, text="", font=("Helvetica", 30))
    spacing_txt.pack(anchor="nw", pady=30, padx=5)

    os_txt = CTkLabel(about_settings, text="StachuOS 4", font=("Helvetica", 30))
    os_txt.pack(anchor="nw", pady=30, padx=5)

    os_build = CTkLabel(about_settings, text="11/25 Build", font=("Helvetica", 30))
    os_build.pack(anchor="nw", pady=30, padx=5)

    os_bit = CTkLabel(about_settings, text="64-bit", font=("Helvetica", 30))
    os_bit.pack(anchor="nw", pady=30, padx=5)

    os_type_installation = CTkLabel(about_settings, text="Modular Installation", font=("Helvetica", 30)) ### CHANGE WHEN MAKING PORTABLE INSTALLATION ###
    os_type_installation.pack(anchor="nw", pady=30, padx=5)

    os_architecture = CTkLabel(about_settings, text="Based on StachuOS zima architecture", font=("Helvetica", 30))
    os_architecture.pack(anchor="nw", pady=30, padx=5)

    os_developers = CTkLabel(about_settings, text="Developed by Stachu Studio ", font=("Helvetica", 30))
    os_developers.pack(anchor="nw", pady=30, padx=5)

def settings_developer():
    global developer_settings
    settings.withdraw()
    developer_settings = ctk.CTkToplevel()
    developer_settings.geometry("1000x1000")
    developer_settings.title("developer settings")
    developer_settings.attributes("-topmost", True)

    back_icon = load_icon("back_arrow_icon", size=(60, 60))
    back_btn = ctk.CTkButton(developer_settings, image=back_icon, text="", fg_color="transparent", hover_color="grey", command=back_settings_developer)
    back_btn.place(y=5, x=5)

    spacing_txt = CTkLabel(developer_settings, text="", font=("Helvetica", 30))
    spacing_txt.pack(anchor="nw", pady=30, padx=5)

    install_devtools_txt = CTkLabel(developer_settings, text="Install developer tools", font=("Helvetica", 40))
    install_devtools_txt.pack(anchor="nw", pady=30, padx=5)

    dev_tools_app_create_btn = CTkButton(developer_settings, text="app creation", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=None)
    dev_tools_app_create_btn.place(x=5, y=200)

    dev_tools_modding_btn = CTkButton(developer_settings, text="Modding", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=None)
    dev_tools_modding_btn.place(x=405, y=200)

    dev_tools_btn = CTkButton(developer_settings, text="Change", fg_color="transparent", font=("Helvetica", 30), hover_color="grey", border_width=2, border_color=("black", "white"), text_color=("black", "white"), command=None)
    dev_tools_btn.place(x=805, y=200)

    spacing2_txt = CTkLabel(developer_settings, text="", font=("Helvetica", 30))
    spacing2_txt.pack(anchor="nw", pady=30, padx=5)


    debug_txt = CTkLabel(developer_settings, text="Debugging", font=("Helvetica", 40))
    debug_txt.pack(anchor="nw", pady=30, padx=5)

    enable_startup_logging_checkbox = CTkCheckBox(developer_settings, text="Show startup logging", font=("Helvetica", 30))
    enable_startup_logging_checkbox.pack(anchor="nw", pady=30, padx=5)

    enable_system_file_explorer_checkbox = CTkCheckBox(developer_settings, text="Show hidden system folders in file explorer", font=("Helvetica", 30))
    enable_system_file_explorer_checkbox.pack(anchor="nw", pady=30, padx=5)

    enable_su_terminal_checkbox = CTkCheckBox(developer_settings, text="Enable super user control in Terminal", font=("Helvetica", 30))
    enable_su_terminal_checkbox.pack(anchor="nw", pady=30, padx=5)

def open_settings():
    global settings
    settings = ctk.CTkToplevel()
    settings.geometry("1000x1000")
    settings.title("settings")
    settings.attributes("-topmost", True)


    settings_account_btn = ctk.CTkButton(
        master=settings,
        text="Account",
        fg_color="transparent",
        text_color=("black", "white"),
        hover_color="grey",
        corner_radius=0,
        font=("Helvetica", 40),
        command=settings_account)

    settings_account_btn.pack(anchor="nw", pady=50, padx=5)


    settings_personalization_btn = ctk.CTkButton(
        master=settings,
        text="Personalization",
        fg_color="transparent",
        text_color=("black", "white"),
        hover_color="grey",
        corner_radius=0,
        font=("Helvetica", 40),
        command=settings_personalization)

    settings_personalization_btn.pack(anchor="nw", pady=50, padx=5)

    settings_apps_btn = ctk.CTkButton(
        master=settings,
        text="Programs",
        fg_color="transparent",
        text_color=("black", "white"),
        hover_color="grey",
        corner_radius=0,
        font=("Helvetica", 40),
        command=settings_personalization)

    settings_apps_btn.pack(anchor="nw", pady=50, padx=5)


    settings_system_btn = ctk.CTkButton(
        master=settings,
        text="System",
        fg_color="transparent",
        text_color=("black", "white"),
        hover_color="grey",
        corner_radius=0,
        font=("Helvetica", 40),
        command=settings_system)

    settings_system_btn.pack(anchor="nw", pady=50, padx=5)


    settings_about_btn = ctk.CTkButton(
    master=settings,
    text="About",
    fg_color="transparent",
    text_color=("black", "white"),
    hover_color="grey",
    corner_radius=0,
    font=("Helvetica", 40),
    command=settings_about)

    settings_about_btn.pack(anchor="nw", pady=50, padx=5)


    settings_developer_btn = ctk.CTkButton(
    master=settings,
    text="Developer",
    fg_color="transparent",
    text_color=("black", "white"),
    hover_color="grey",
    corner_radius=0,
    font=("Helvetica", 40),
    command=settings_developer)

    settings_developer_btn.pack(anchor="nw", pady=50, padx=5)

