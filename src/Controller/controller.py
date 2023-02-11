from View import View
from Model import Model

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
		if self.model.users_manager.login(username, password):
			self.view.hide_page("login")
			self.view.title("Hybrid")
			self.view.show_page("home")
			self.view.show_menu()
			self.view.resizable(True, True)
		else:
			self.view.pages.get("login").login_error()

	def show_page(self, name):
		self.view.show_page(name)


