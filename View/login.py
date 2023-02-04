import tkinter as tk
from tkinter import ttk
from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTkButton


class Login(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Login
        self.login = CTkFrame(
            master=parent, fg_color="black")
        self.login.pack_propagate("False")
        self.login.pack(expand=True, fill="both")

        # EntrysContainer
        self.entrysContainer = CTkFrame(
            master=self.login, fg_color="transparent")
        self.entrysContainer.pack(expand=True, ipady=40, ipadx=40)

        # Username
        self.username_var = tk.StringVar(value="")
        self.username_entry = CTkEntry(
            master=self.entrysContainer, width=150, placeholder_text="Username", placeholder_text_color="black", text_color="white", fg_color="white", font=("Open Sans ExtraBold", 14))
        self.username_entry.configure(
            self, corner_radius=27, border_width=0, justify="center")
        self.username_entry.pack(expand=True, ipady=5, ipadx=5)

        # Password
        self.password_var = tk.StringVar(value="")
        self.password_entry = CTkEntry(
            master=self.entrysContainer, width=150, placeholder_text="Password", placeholder_text_color="black", text_color="white", fg_color="white", font=("Open Sans ExtraBold", 14))
        self.password_entry.configure(
            corner_radius=27, border_width=0, show="*", justify="center")
        self.password_entry.pack(expand=True, ipady=5, ipadx=5)

        # ButtonLogin
        self.button_login = CTkButton(
            master=self.entrysContainer, text="Login", width=100)
        self.button_login.configure(
            corner_radius=27, border_width=0, fg_color="#C92C37", hover_color="#990510", text_color="black", font=("Open Sans ExtraBold", 14))
        self.button_login.pack(expand=True, ipady=5, ipadx=5)

        # ButtonRegister
        self.button_register = CTkButton(
            master=self.entrysContainer, text="Register", width=50)
        self.button_register.configure(
            corner_radius=27, border_width=0, fg_color="black", hover_color="#C92C37", text_color="white", font=("Open Sans Light", 14))
        self.button_register.pack(expand=True)


if __name__ == "__main__":
    pass
