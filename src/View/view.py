from customtkinter import CTk, CTkLabel
from View.login import Login
from View.register import Register
from View.menu import Menu
from View.home import Home
from View.about import About
from View.stock import Stock


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

	def set_controller(self, controller):
		for page in self.pages.values():
			page.set_controller(controller)

	def show_login(self):
		self.current_page.pack(ipadx=20, ipady=20)
		self.resizable(False, False)

	def show_menu(self):
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

		message_error = CTkLabel(
			self.current_page,
			text = message,
			# text_color = SECONDARY,
			# fg_color = BLACK,
			corner_radius = 27
		)
		message_error.pack(side="bottom", padx=20, pady=10)
		self.after(1000,lambda:self.set_default(message_error,buttons))

	def set_default(self,message_error,buttons):
		for button in buttons:
			button.configure(state="normal")
		message_error.pack_forget()
