class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def check(self, username:str):
		"""
		username
		"""
		if username == "juan":
			self.view.hide_login()
			self.view.show_home()

