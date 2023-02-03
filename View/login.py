import tkinter as tk
from tkinter import ttk


class Login(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # username
        self.username_var = tk.StringVar(value="Username")
        self.username_entry = ttk.Entry(
            self, textvariable=self.username_var, width=30)
        self.username_entry.pack()
        # password
        self.password_var = tk.StringVar(value="Password")
        self.password_entry = ttk.Entry(
            self, textvariable=self.password_var, width=30)
        self.password_entry.pack()

        # buttonLogin
        self.button_login = ttk.Button(self, text="Login")
        self.button_login.pack()

        # buttonRegister
        self.register = ttk.Button(self, text="Register")
        self.register.pack()


if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    login.pack()
    root.mainloop()
