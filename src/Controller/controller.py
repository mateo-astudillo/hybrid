from View import View
from Model import Model

class Controller:
	def __init__(self, model:Model, view:View):
		self.model = model
		self.view = view

	def run(self):
		self.view.show_login()

	def login(self, username:str, password:str):
		"""
		username
		password
		"""
		self.model.login(username, password)
		self.view.hide_page("login")
		self.view.show_menu()
		self.view.show_page("home")

	def get_credentials(self):
		return self.model.get_credentials()

	def show_page(self, name):
		self.view.show_page(name)


