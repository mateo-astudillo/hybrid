import tkinter as tk
from tkinter import ttk
from customtkinter import CTk
from View import login


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry("350x550")


if __name__ == '__main__':
    app = App()
    loginFrame = login.Login(app)
    app.mainloop()
