from customtkinter import *
import customtkinter as ctk

notifications = []
notification_frame = None

def add_notification(title, message):
    notifications.append((title, message))



def open_notification_frame():
    global notification_frame
    from desktop import home
    from config_read import taskbar_colour


    notification_frame = CTkFrame(home, fg_color=taskbar_colour, height=1372, width=500, border_color=("black", "white"), border_width=3)
    notification_frame.place(y=3, x=2055)


    close_notification_frame_btn = CTkButton(
        notification_frame,
        text="X",
        fg_color="transparent",
        text_color=("black", "white"),
        hover_color="grey",
        command=notification_frame.destroy,
        width=30, font=("Arial", 45)
    )
    close_notification_frame_btn.place(x=5, y=5)


    notification_frame_title = CTkLabel(
        notification_frame, text="Notifications",
        font=("Arial", 40), text_color=("black", "white")
    )
    notification_frame_title.place(x=145, y=10)


    display_notifications()


def display_notifications():
    global notification_frame
    if notification_frame is None:
        return

    y = 100
    for i, (title, message) in enumerate(notifications):
        notif = ctk.CTkFrame(
            notification_frame,
            fg_color="#222222",
            corner_radius=10,
            width=480,
            height=70
        )
        notif.place(x=10, y=y)

        title_label = ctk.CTkLabel(notif, text=title, font=("Arial", 16, "bold"))
        title_label.place(x=10, y=5)

        message_label = ctk.CTkLabel(notif, text=message, font=("Arial", 13))
        message_label.place(x=10, y=35)


        close_btn = ctk.CTkButton(
            notif,
            text="X",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="red",
            command=lambda n=notif, idx=i: remove_notification(n, idx)
        )
        close_btn.place(x=440, y=20)

        y += 80

def remove_notification(notif_frame, index):
    notif_frame.destroy()
    del notifications[index]


