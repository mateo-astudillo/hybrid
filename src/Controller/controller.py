class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def login(self, username:str, password:str):
		"""
		username
		password
		"""
		# Validate
		self.model.login(username, password)
		self.view.hide_login()
		self.view.show_main_page()
		# if username == "":
		# 	self.view.show_alert()

	def get_credentials(self):
		return self.model.get_credentials()

