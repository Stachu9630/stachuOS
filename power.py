from customtkinter import *
from ctk_components import *
import customtkinter as ctk
import subprocess


def back_btn_pressed():
    power.destroy()

def power_shutdown():    
    
    def shutdown():
        exit()

    shutdown_screen = CTkToplevel()
    shutdown_screen.attributes("-fullscreen", True)
    shutdown_screen.attributes("-topmost", True)
    shutdown_screen.configure(fg_color="#000000")

    shutdown_text = CTkLabel(shutdown_screen, text="Shutting down", font=("Arial", 50), text_color="white")
    shutdown_text.pack(pady=500)

    shutdown_screen.after(1000, shutdown)


def power_restart():
    def restart():
        from root import root1
        from root import start_root
        root1.destroy()
        start_root()
    restart_screen = CTkToplevel()
    restart_screen.attributes("-fullscreen", True)
    restart_screen.attributes("-topmost", True)
    restart_screen.configure(fg_color="#000000")
    CTkLabel(restart_screen, text="Restarting", font=("Arial", 50), text_color="white").pack(pady=500)


    ####################################################################
    #does not work
    #fix
    ####################################################################


    restart_screen.after(1000, restart)






def power_sleep():

    sleep_screen = CTkToplevel()
    sleep_screen.attributes("-fullscreen", True)
    sleep_screen.attributes("-topmost", True)
    sleep_screen.configure(fg_color=("#000000"))

def power_signout():

    signout_screen = CTkToplevel()
    signout_screen.attributes("-fullscreen", True)
    signout_screen.attributes("-topmost", True)
    signout_screen.configure(fg_color="#000000")

def power_lock():

    lock_screen = CTkToplevel()
    lock_screen.attributes("-fullscreen", True)
    lock_screen.attributes("-topmost", True)
    lock_screen.configure(fg_color="#000000")

def power_options():
    global power
    power = CTkToplevel()
    power.attributes("-fullscreen", True)
    #power.attributes("-topmost", True)

    shutdown_btn = CTkButton(
        master=power,
        text="Shutdown",
        fg_color="transparent",
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=power_shutdown)

    shutdown_btn.pack(padx=10, pady=85)

    restart_btn = CTkButton(
        master=power,
        text="Restart",
        fg_color="transparent",
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=power_restart)

    restart_btn.pack(padx=10, pady=85)

    sleep_btn = CTkButton(
        master=power,
        text="Sleep",
        fg_color="transparent",
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=power_sleep)

    sleep_btn.pack(padx=10, pady=85)

    signout_btn = CTkButton(
        master=power,
        text="Signout",
        fg_color="transparent",#
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=power_signout)

    signout_btn.pack(padx=10, pady=85)

    lock_btn = CTkButton(
        master=power,
        text="Lock",
        fg_color="transparent",
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=power_lock)

    lock_btn.pack(padx=10, pady=85)

    back_btn = CTkButton(
        master=power,
        text="Back",
        fg_color="transparent",
        text_color=("#000000", "#ffffff"),
        corner_radius=0,
        font=("Helvetica", 30),
        command=back_btn_pressed
    )

    back_btn.pack(padx=10, pady=100)

def desktop_power_options(event=None):

    #SAMPLE CODE#
    #CHANGE#
    from desktop import home

    BTN_OPTION = {
        "compound": "left",
        "anchor": "w",
        "fg_color": "transparent",
        "text_color": ("black", "white"),
        "corner_radius": 5,
        "hover_color": ("gray90", "gray25")
    }

    desktop_power_popup = CTkPopupMenu(master=home, width=250, height=270, title="Title", corner_radius=8, border_width=0)
    home.bind("<F1>", lambda event: do_popup(event, desktop_power_popup), add="+")


    btn1 = ctk.CTkButton(desktop_power_popup.frame, text="Shutdown", command=power_shutdown, **BTN_OPTION)
    btn1.pack(expand=True, fill="x", padx=10, pady=0)

    btn2 = ctk.CTkButton(desktop_power_popup.frame, text="Restart", command=power_restart, **BTN_OPTION)
    btn2.pack(expand=True, fill="x", padx=10, pady=(1, 0))

    btn3 = ctk.CTkButton(desktop_power_popup.frame, text="Signout", command=power_signout, **BTN_OPTION)
    btn3.pack(expand=True, fill="x", padx=10, pady=(1, 0))

