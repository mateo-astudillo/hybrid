from View import View
from Model import Model
from re import match
from . import LoginC

class Controller:
	def __init__(self, model:Model, view:View):
		self.model = model
		self.view = view
		self.pages = {
			"login": 
		}

	def run(self):
		self.view.title("Login")
		self.view.show_login()
		self.view.mainloop()

	def register(self, username:str, password:str):
		if match("^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$",username) is not None:
			self.model.users_manager.register(username, password)
			self.view.show_page("login")
		else:
			self.view.error("Error with symbols",self.view.pages.get("register").buttons.values())

	def show_page(self, name):
		self.view.show_page(name)


