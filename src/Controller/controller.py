class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def login(self, username:str, password:str):
		"""
		username
		password
		"""
		if username == "juan":
			self.view.hide_login()
			self.view.show_main_page()

