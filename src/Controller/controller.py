from View import View
from Model import Model
from re import match

class Controller:
	def __init__(self, model:Model, view:View):
		self.model = model
		self.view = view

	def run(self):
		self.view.title("Login")
		self.view.show_login()
		self.view.mainloop()

	def login(self, username:str, password:str):
		"""
		username
		password
		"""
		# if match("^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$",username) is not None:
		if self.model.users_manager.login(username, password):
			self.view.hide_page("login")
			self.view.title("Hybrid")
			self.view.show_page("home")
			self.view.show_menu()
			self.view.resizable(True, True)
		else:
			self.view.error("Incorrect Password or Username")

	def register(self, username:str, password:str):
		if match("^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$",username) is not None:
			self.model.users_manager.register(username, password)
			self.view.show_page("login")
		else:
			self.view.error("Error with symbols",self.view.pages.get("register").buttons.values())

	def show_page(self, name):
		self.view.show_page(name)


