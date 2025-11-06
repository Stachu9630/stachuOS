from logger import log
log("config_read module alive")

default = None

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        log(f"[read_file] Missing file: {path}")
        return default

language = read_file("configs/STACONFIG/Language.staconfig")
log("language: " + language)

username = read_file("configs/STACONFIG/username.staconfig")
log("username: " + username)

password = read_file("configs/STACONFIG/Password.staconfig")
log("password: " + password)

login_screen = read_file("configs/STACONFIG/login_screen.staconfig")
log("login_screen: " + login_screen)

terminal_password_require = read_file("configs/STACONFIG/shell_password_require.staconfig")
log("terminal_password_require: " + terminal_password_require)

dark_mode = read_file("configs/STACONFIG/dark_mode.staconfig")
log("dark_mode: " + dark_mode)

wallpaper_colour = read_file("configs/STACONFIG/wallpaper_colour.staconfig")
log("wallpaper_colour: " + wallpaper_colour)

taskbar_colour = read_file("configs/STACONFIG/taskbar_colour.staconfig")
log("taskbar_colour: " + taskbar_colour)

desktop_look = read_file("configs/STACONFIG/desktop_look.staconfig")
log("desktop_look: " + desktop_look)

desktop_name = read_file("configs/STACONFIG/desktop_name.staconfig")
log("desktop_name: " + desktop_name)

account_icon = read_file("configs/STACONFIG/account_icon.staconfig")
log("account_icon: " + account_icon)

icon_pack = read_file("configs/STACONFIG/icon_pack.staconfig")
log("icon_pack: " + icon_pack)
