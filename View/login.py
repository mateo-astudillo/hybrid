import tkinter as tk
from tkinter import ttk
from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image


class Login(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #! Login
        self.login = CTkFrame(
            master=parent, fg_color="black")
        self.login.pack_propagate("False")
        self.login.pack(expand=True, fill="both")

        #! ImgContainer
        self.imgContainer = CTkFrame(master=self.login, fg_color="blue")
        self.imgContainer.pack_propagate("False")
        self.imgContainer.pack(fill="both")

        #! Image
        self.my_image = CTkImage(
            dark_image=Image.open("logo.jpg"), size=(500, 250))

        self.image = CTkLabel(
            master=self.imgContainer,
            image=self.my_image,
            text="", )

        self.image.pack(fill="both")

        #! EntrysContainer
        self.entrysContainer = CTkFrame(
            master=self.login, fg_color="transparent")
        self.entrysContainer.pack(pady=10, ipady=55, ipadx=40)

        #! Username
        self.username_var = tk.StringVar(value="")

        self.username_entry = CTkEntry(
            master=self.entrysContainer,
            width=180,
            placeholder_text="Username",
            placeholder_text_color="black",
            text_color="black",
            fg_color="#fff",
            font=("Open Sans ExtraBold", 14))

        self.username_entry.configure(
            self, corner_radius=27,
            border_width=0,
            justify="center")

        self.username_entry.pack(expand=True, ipady=1, ipadx=5)

        #! Password
        self.password_var = tk.StringVar(value="")
        self.password_entry = CTkEntry(
            master=self.entrysContainer,
            width=180,
            placeholder_text="Password",
            placeholder_text_color="black",
            text_color="black", fg_color="#fff",
            font=("Open Sans ExtraBold", 14))

        self.password_entry.configure(
            corner_radius=27,
            border_width=0,
            show="*",
            justify="center")

        self.password_entry.pack(expand=True, ipady=1, ipadx=7)

        #!! ButtonLogin
        self.button_login = CTkButton(
            master=self.entrysContainer, text="Login", width=180)

        self.button_login.configure(
            corner_radius=27,
            border_width=0,
            fg_color="#C92C37",
            hover_color="#990510",
            text_color="black",
            font=("Open Sans ExtraBold", 14))

        self.button_login.pack(expand=True, ipady=1, ipadx=5)

        #! ButtonRegister
        self.button_register = CTkButton(
            master=self.entrysContainer,
            text="Register",
            width=50)

        self.button_register.configure(
            corner_radius=27,
            border_width=0,
            fg_color="black",
            hover_color="#C92C37",
            text_color="#fff",
            font=("Open Sans Light", 14))

        self.button_register.pack()


if __name__ == "__main__":
    pass
