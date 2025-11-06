from customtkinter import *
from PIL import Image
from CTkColorPicker import AskColor
from CTkMessagebox import CTkMessagebox
from logger import log

taskbar_colour = ""
wallpaper_colour = ""
account_icon_chosen = None

def start_setup():

    def save_setup():
        def restart():
            setup.destroy()
            save_setup_screen.destroy()
            from root import start_root
            start_root()

        save_setup_screen = CTkToplevel()
        save_setup_screen.attributes("-topmost", True)
        save_setup_screen.attributes("-fullscreen", True)
        save_setup_screen.configure(fg_color="#000000")

        img_save_setup = CTkImage(light_image=Image.open("icons/file_save.png"), dark_image=Image.open("icons/file_save.png"), size=(200, 200))
        txt_save_setup = CTkLabel(save_setup_screen, image=img_save_setup, text="")
        txt_save_setup.pack(pady=500)
        


        with open ("configs/STACONFIG/Language.staconfig", "w") as file:
            file.write(optionMenu_setup_lang.get())
            file.close()

        with open ("configs/STACONFIG/username.staconfig", "w") as file:
            file.write(entry_setup_username.get())
            file.close()

        with open ("configs/STACONFIG/Password.staconfig", "w") as file:
            file.write(entry_setup_password.get())
            file.close()

        with open ("configs/STACONFIG/login_screen.staconfig", "w") as file:
            file.write(checkbox_setup_loginScreen.get())
            file.close()

        with open ("configs/STACONFIG/shell_password_require.staconfig", "w") as file:
            file.write(checkbox_setup_shellPasswordRequire.get())
            file.close()

        with open ("configs/STACONFIG/dark_mode.staconfig", "w") as file:
            file.write(checkbox_setup_dark_mode.get())
            file.close()

        with open ("configs/STACONFIG/wallpaper_colour.staconfig", "w") as file:
            file.write(wallpaper_colour)
            file.close()

        with open ("configs/STACONFIG/taskbar_colour.staconfig", "w") as file:
            file.write(taskbar_colour)
            file.close()

        with open ("configs/STACONFIG/desktop_look.staconfig", "w") as file:
            file.write(optionMenu_desktopLook_setup.get())
            file.close()

        with open ("configs/STACONFIG/desktop_name.staconfig", "w") as file:
            file.write(entry_desktopName_setup.get())
            file.close()
        
        with open ("configs/STACONFIG/acc_icon_default.staconfig", "w") as file:
            file.write(account_icon_chosen)
        open("configs/NRfiles/setup_complete.NR", "w").close()
        log("setup complete saved")

        save_setup_screen.after(1000, lambda : restart)

    def final_setup():
        scrollFrame_apps.place_forget()



        finish_setup = CTkButton(setup_frame, text="Finish", command=save_setup, width=30)
        finish_setup.place(x=500, y=610)

    def app_setup():
        global scrollFrame_apps


        setup_progress.set(0.80)

        scrollFrame_apps = CTkScrollableFrame(setup_frame, label_text="Choose apps to download", width=300, height=400)
        scrollFrame_apps.place(anchor="center", x=175, y=275)

        next_apps = CTkButton(setup_frame, text="Next", command=final_setup, width=30)
        next_apps.place(x=500, y=610)
            
    def customization_setup_desktop_look():
        acc_icon_explainer.place_forget()
        scrollFrame_accicons.place_forget()
        for btn in buttons:
            btn.place_forget()


        
    def customization_setup_acc_icons():
        global account_icon_chosen
        global acc_icon_explainer, scrollFrame_accicons
        global buttons, next_accicon_customization


        if taskbar_colour == "":
            warning3 = CTkMessagebox(title="Stachu OS Setup", message="No taskbar colour selected", icon="warning", option_1="Ok")

        else:

            if wallpaper_colour == "":
                warning4 = CTkMessagebox(title="Stachu OS Setup", message="No wallpaper colour selected", icon="warning", option_1="Ok")

            else:
                txt_setup_customize.place_forget()
                checkbox_setup_dark_mode.place_forget()
                btn_wallpaper_setup.place_forget()
                txt_wallpaper_setup.place_forget()
                btn_taskbar_setup.place_forget()
                txt_taskbar_setup.place_forget()
                txt_desktopLook_setup.place_forget()
                optionMenu_desktopLook_setup.place_forget()
                txt_desktopName_setup.place_forget()
                entry_desktopName_setup.place_forget()
                next_customization.place_forget()
                
                acc_icon_explainer = CTkLabel(setup_frame, text="""
                What are account icons used for?
                
                Account icons are shown on the
                start menu and only a cosmetic
                feature for the user to
                personalise thier OS
                
                You can change to a different
                account icon later in settings""", justify="left", font=("Arial", 14))
                acc_icon_explainer.place(anchor="center", x=428, y=150)
        
        
                scrollFrame_accicons = CTkScrollableFrame(setup_frame, label_text="Choose your account icon", width=300, height=400)
                scrollFrame_accicons.place(anchor="center", x=175, y=275)


                account_icons = [
                    ("account_icon_light", "account_icon_dark", 25, 100),
                    ("account_icon_red", "account_icon_red", 25, 150),
                    ("account_icon_light_blue", "account_icon_light_blue", 25, 200),
                    ("account_icon_dark_blue", "account_icon_dark_blue", 25, 250),
                    ("account_icon_green", "account_icon_green", 25, 300),
                    ("account_icon_yellow", "account_icon_yellow", 175, 100),
                    ("account_icon_orange", "account_icon_orange", 175, 150),
                    ("account_icon_pink", "account_icon_pink", 175, 200),
                    ("account_icon_purple", "account_icon_purple", 175, 250),
                ]
                
                buttons = []
                
                for light_name, dark_name, x_pos, y_pos in account_icons:
                    icon = CTkImage(
                        light_image=Image.open(f"icons/{light_name}.png"),
                        dark_image=Image.open(f"icons/{dark_name}.png"),
                        size=(40, 40)
                    ) 
                    btn = CTkButton(
                        setup_frame,
                        image=icon,
                        text="",
                        fg_color="transparent",
                        hover_color="grey",
                        border_width=1,
                        border_color="white"
                    )
                    btn.place(x=x_pos, y=y_pos)
                    buttons.append(btn)
        
                next_accicon_customization = CTkButton(setup_frame, text="Next", command=customization_setup_desktop_look, width=30)
                next_accicon_customization.place(x=500, y=610)
            
        

    def customization_setup():
        global txt_setup_customize, checkbox_setup_dark_mode, btn_wallpaper_setup, txt_wallpaper_setup, btn_taskbar_setup, txt_taskbar_setup, txt_desktopLook_setup, optionMenu_desktopLook_setup, txt_desktopName_setup, entry_desktopName_setup
        global next_customization, wallpaper_colour, taskbar_colour
    
        def choose_wallpaper_colour():
            global wallpaper_colour
            pick_color = AskColor()
            wallpaper_colour = pick_color.get()
            btn_wallpaper_setup.configure(fg_color=wallpaper_colour)
    
        def choose_taskbar_colour():
            global taskbar_colour
            pick2_color = AskColor()
            taskbar_colour = pick2_color.get()
            btn_taskbar_setup.configure(fg_color=taskbar_colour)

        if entry_setup_username.get() == "":
            warning = CTkMessagebox(title="Stachu OS Setup", message="No username entered", icon="warning", option_1="Ok")
    
        elif entry_setup_password.get() == "":
            warning2 = CTkMessagebox(title="Stachu OS Setup", message="No password entered", icon="warning", option_1="Ok")
    
        else:
            txt_setup_login.place_forget()
            txt_setup_username.place_forget()
            entry_setup_username.place_forget()
            entry_setup_password.place_forget()
            txt_setup_password.place_forget()
            checkbox_setup_loginScreen.place_forget()
            checkbox_setup_shellPasswordRequire.place_forget()
            next_login.place_forget()
    
            setup_progress.set(0.40)
            
    
    
            txt_setup_customize = CTkLabel(setup_frame, text="Choose your customization settings", font=("Arial", 20))
            txt_setup_customize.place(anchor="center", x=275, y=25)   
            checkbox_setup_dark_mode = CTkCheckBox(setup_frame, text="Dark Mode", font=("Arial", 20), onvalue = "True", offvalue = "False")
            checkbox_setup_dark_mode.place(anchor="center", x=75, y=100)
    
            btn_wallpaper_setup = CTkButton(setup_frame, text="Select", font=("Arial", 20), width=50, fg_color = "#757171", command=choose_wallpaper_colour)
            btn_wallpaper_setup.place(anchor="center", x=40, y=150)
    
            txt_wallpaper_setup = CTkLabel(setup_frame, text="Wallpaper colour", font=("Arial", 20))
            txt_wallpaper_setup.place(anchor="center", x=155, y=150)
    
            btn_taskbar_setup = CTkButton(setup_frame, text="Select", font=("Arial", 20), width=50, fg_color = "#757171", command=choose_taskbar_colour)
            btn_taskbar_setup.place(anchor="center", x=40, y=200)
    
            txt_taskbar_setup = CTkLabel(setup_frame, text="Taskbar colour", font=("Arial", 20))
            txt_taskbar_setup.place(anchor="center", x=145, y=200)
    
            txt_desktopLook_setup = CTkLabel(setup_frame, text="Desktop look", font=("Arial", 20))
            txt_desktopLook_setup.place(anchor="center", x=65, y=250)
    
            optionMenu_desktopLook_setup = CTkOptionMenu(setup_frame, values=["New", "Legacy"], width=30)
            optionMenu_desktopLook_setup.place(anchor="center", x=180, y=250)
    
            txt_desktopName_setup = CTkLabel(setup_frame, text="Desktop Name", font=("Arial", 20))
            txt_desktopName_setup.place(anchor="center", x=75, y=300)
    
            entry_desktopName_setup = CTkEntry(setup_frame, font=("Arial", 20))
            entry_desktopName_setup.place(anchor="center", x=220, y=300)
    
            next_customization = CTkButton(setup_frame, text="Next", command=customization_setup_acc_icons, width=30)
            next_customization.place(x=500, y=610)

    def login_setup():
        setup_progress.set(0.15)
        txt_setup_lang_title.place_forget()
        txt_setup_lang.place_forget()
        optionMenu_setup_lang.place_forget()
        next_general.place_forget()

        global txt_setup_login, txt_setup_username, txt_setup_password, entry_setup_username, entry_setup_password, next_login, checkbox_setup_loginScreen, checkbox_setup_shellPasswordRequire
        
        txt_setup_login = CTkLabel(setup_frame, text="Security", font=("Arial", 20))
        txt_setup_login.place(anchor="center", x=275, y=25)

        txt_setup_username = CTkLabel(setup_frame, text="Username", font=("Arial", 20))
        txt_setup_username.place(anchor="nw", y=110, x=10)

        entry_setup_username = CTkEntry(setup_frame, width=300, font=("Arial", 20))
        entry_setup_username.place(y=110, x=130)

        txt_setup_password = CTkLabel(setup_frame, text="Password", font=("Arial", 20))
        txt_setup_password.place(anchor="nw", y=160, x=10)

        entry_setup_password = CTkEntry(setup_frame, width=300, font=("Arial", 20))
        entry_setup_password.place(y=160, x=130)

        checkbox_setup_loginScreen = CTkCheckBox(setup_frame, text="Login Screen", font=("Arial", 20), onvalue = "True", offvalue = "False")
        checkbox_setup_loginScreen.place(anchor="center", x=75, y=250)

        checkbox_setup_shellPasswordRequire = CTkCheckBox(setup_frame, text="Require Password For Shell", font=("Arial", 20), onvalue = "True", offvalue = "False")
        checkbox_setup_shellPasswordRequire.place(anchor="center", x=141, y=300)

        next_login = CTkButton(setup_frame, text="Next", command=customization_setup, width=30)
        next_login.place(x=500, y=610)

    def general_setup():
        global txt_setup_lang_title, txt_setup_lang, optionMenu_setup_lang, scrollFrame_time, next_general, selected_timezone
        log("general setup started")
        setup_progress.set(0.05)


        txt_setup_lang_title = CTkLabel(setup_frame, text="General Options", font=("Arial", 20))
        txt_setup_lang_title.place(anchor="center", x=275, y=25)

        txt_setup_lang = CTkLabel(setup_frame, text="Language", font=("Arial", 20))
        txt_setup_lang.place(anchor="center", y=110, x=50)

        optionMenu_setup_lang = CTkOptionMenu(setup_frame, values=["English", "Polish"])
        optionMenu_setup_lang.place(anchor="center", x=185, y=110)

        next_general = CTkButton(setup_frame, text="Next", command=login_setup, width=30)
        next_general.place(x=500, y=610)

    def start_btn_pressed():
        log("start setup btn pressed")
        btn_setup_start.place_forget()
        log("start setup button forgotten")
        txt_setup_welcome.place_forget()
        log("start welcome text forgotten")

        general_setup()
        log("general setup called")

    setup = CTk()
    log("setup created")
    setup.attributes("-fullscreen", True)
    setup_progress = CTkProgressBar(setup, orientation="horizontal", width=3000, height=30)

    setup_progress.set(0)
    setup_progress.pack(pady=30, padx=10, anchor="nw")
    log("progress bar created")

    spacing1 = CTkLabel(setup, text="", font=("Arial", 20))
    spacing1.pack(pady=200)

    setup_frame = CTkFrame(setup, width=550, height=650)
    setup_frame.pack()
    log("frame created")

    txt_setup_welcome = CTkLabel(setup_frame, text="StachuOS setup", font=("Arial", 20))
    txt_setup_welcome.place(x=200, y=25)

    btn_setup_start = CTkButton(setup_frame, text="Start setup", command = start_btn_pressed)
    btn_setup_start.place(x=200, y=130)


    setup.mainloop()
    exit()
    
#start_setup()
