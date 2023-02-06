from customtkinter import CTkFrame
from View.home import Home
from View.login import Login

class View(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.login = Login(self)
        self.home = Home(self)


    def show_home(self):
        self.home.pack()
    
    def hide_login(self):
        self.login.destroy()

