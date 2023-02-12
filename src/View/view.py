from customtkinter import CTk, CTkLabel
from time import sleep
from View.login import Login
from View.register import Register
from View.menu import Menu
from View.home import Home
from View.about import About
from View.stock import Stock

BLACK = "#000000"
BACKGROUND = "#8D99AE"
WHITE = "#EDF2F4"
SECONDARY = "#EF233C"
PRIMARY = "#D90429"


class View(CTk):
	def __init__(self):
		super().__init__()

		self.pages = {
			"login": Login(self),
			"register": Register(self),
			"menu": Menu(self),
			"home": Home(self),
			"stock": Stock(self),
			"about": About(self),
		}

		self.current_page = self.pages.get("login")

		self.set_config()

	def set_controller(self, controller):
		for page in self.pages.values():
			page.set_controller(controller)

	def set_config(self):
		for page in self.pages.values():
			page.configure(fg_color=BLACK, bg_color=BLACK)

	def show_login(self):
		self.current_page.pack(ipadx=20, ipady=20)
		self.resizable(False, False)

	def show_menu(self):
		self.pages.get("menu").set_config()
		self.pages.get("menu").pack(side="left", fill="y", expand=False)

	def hide_page(self, name_page:str):
		self.pages.get(name_page).pack_forget()

	def show_page(self, name_page:str):
		self.current_page.pack_forget()
		self.current_page = self.pages.get(name_page)
		self.current_page.pack(ipadx=20, ipady=20, side="right", fill="both", expand=True)

	def error(self, message,buttons):
		for button in buttons:
			button.configure(state="disabled")

		message_error = CTkLabel( #!Le cambie de message a message_error porque message lo usabamos en la property
			self.current_page,
			text = message,
			text_color = SECONDARY,
			fg_color = BLACK,
			corner_radius = 27
		)
		message_error.pack(side="bottom", padx=20, pady=10) #! Le hago el pack por separado, porque si no message_error guardaba NONE, por eso no hacia pack_forget()
		self.after(1000,lambda:self.set_default(message_error,buttons)) #! Uso after por que esta hecho para esto, pero solo funciona en master, es decir ahora en register

	def set_default(self,message_error,buttons): #!Esta funcion la podes quitar y poner esto arriba, pero a after le tenes que pasar el tiempo y una funcion
		for button in buttons:
			button.configure(state="normal")
		message_error.pack_forget()
