from User.user import User
from User.model import Model
from User.view import View


class Logic:
	def __init__(self, model:Model, view:View, user:User):
		self.view = view
		self.model = model
		self.user = user

	def login(self) -> bool:
		if not self.model.login(self.user.username, self.user.password):
			# show error
			return False
		# show ok
		self.user.logged = True
		return True



