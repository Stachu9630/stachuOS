import customtkinter
from CTkMessagebox import CTkMessagebox
from customtkinter import *
import desktop
from logger import log
from config_read import login_screen, username, password, dark_mode
import customtkinter as ctk


log("login module logging alive !")
login_pass = None

if dark_mode == "True":
    customtkinter.set_appearance_mode("Dark")
    log("dark mode set")

else:
    customtkinter.set_appearance_mode("Light")
    log("light mode set")
    
    
def login_btn_pressed():

    if login_pass.get() == password:
        log("password correct")
        login.destroy()
        log("login window destroyed")
        desktop.desktop_ui()
        log("desktop ui started")
        
    else:
        log("password incorrect")
        msg = CTkMessagebox(
            title="Stax",
            message="Incorrect password",
            icon="cancel",
            option_1="Ok")

def login_start():
    global login, login_pass
    if login_screen == "True":

        log("login GUI started")


        login = CTk()
        login.attributes("-fullscreen", True)

        login_user = ctk.CTkLabel(login, text=username, font=("Helvetica", 65))
        login_user.pack(pady=200)

        login_pass = ctk.CTkEntry(login, width=450, height=40, font=("Helvetica", 25))
        login_pass.pack()

        login_stax = ctk.CTkLabel(login, text="secured by Stax", font=("Helvetica", 18))
        login_stax.place(x=1370, y=520)

        login_enter = ctk.CTkButton(
            login,
            height=35,
            width=125,
            text="login",
            fg_color="transparent",
            text_color=("black", "white"),
            border_width=2,
            border_color=("black", "white"),
            font=("Helvetica", 20),
            hover_color="gray",
            command=login_btn_pressed
        )

        login_enter.pack(pady=50)

        login.mainloop()

    elif login_screen == "False":
        log("login GUI started")

        login = CTk()
        login.attributes("-fullscreen", True)

        login_user = ctk.CTkLabel(login, text=username, font=("Helvetica", 65))
        login_user.pack(pady=200)

        login_simple_enter = ctk.CTkButton(
            login,
            height=35,
            width=125,
            text="login",
            fg_color="transparent",
            text_color=("black", "white"),
            border_width=2,
            border_color=("black", "white"),
            font=("Helvetica", 20),
            hover_color="gray",
            command=(lambda: (login.destroy(), desktop.desktop_ui(), )) #Huh this actually works?
        )

        login_simple_enter.pack(pady=50)




        login.mainloop()
