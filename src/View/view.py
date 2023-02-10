from View.login import Login
from View.menu import Menu
from View.home import Home
from View.about import About


class View():
	def __init__(self, master=None):

		self.pages = {
			"login": Login(master),
			"menu": Menu(master),
			"home": Home(master),
			# "Stock": Stock(master),
			"about": About(master),
		}

		self.current_page = self.pages.get("login")
	
	def set_controller(self, controller):
		for page in self.pages.values():
			page.set_controller(controller)

	def set_config(self):
		for page in self.pages.values():

			page.configure(width=800, height=900)
		self.pages.get(Menu).conconfigure(width=400)

	def show_login(self):
		self.current_page.pack(ipadx=20, ipady=20)

	def show_menu(self):
		self.pages.get("menu").pack(side="left", fill="y", expand=False)
	
	def hide_page(self, name_page:str):
		self.pages.get(name_page).pack_forget()

	def show_page(self, name_page:str):
		self.current_page.pack_forget()
		self.current_page = self.pages.get(name_page)
		self.current_page.pack(ipadx=20, ipady=20, side="right", fill="both", expand=True)
