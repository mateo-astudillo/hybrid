import tkinter as tk
from tkinter import ttk
from customtkinter import CTk
from View.login import Login


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.resizable(False, False)
        self.geometry("350x530")


if __name__ == '__main__':
    app = App()
    loginFrame = Login(app)
    app.mainloop()
