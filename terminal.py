from customtkinter import *
from config_read import terminal_password_require




def run_command(entered_command):
    pass

def setup_cmd():
    pass

def start_cmd():
    cmd_window = CTkToplevel()
    cmd_window.title("Terminal")
    cmd_window.geometry("750x500")
    cmd_window.attributes("-topmost", True)
    cmd_window.configure(fg_color="black")

    cmd_entry = CTkEntry(cmd_window, placeholder_text="Enter command", fg_color="black")
    cmd_entry.pack(pady=20)

def open_cmd():
    if terminal_password_require == "True":
        dialog = CTkInputDialog(text="Enter Password:", title="Password required to open terminal")
    else:
        start_cmd()







