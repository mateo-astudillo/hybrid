from customtkinter import CTkFrame
from View.login import Login
from View.menu import Menu
from View.home import Home


class View(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.menu = Menu(self)
		self.home = Home(self)
		self.login = Login(self)


	def show_main_page(self):
		self.menu.pack(side="left")
		self.home.pack(side="right")
	
	def hide_login(self):
		self.login.pack_forget()

