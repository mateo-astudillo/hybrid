from re import match


class User:
	def __init__(self):
		self.logged = False
		self.username = None
		self.password = None

	def set_username(self, username:str) -> bool:
		pattern = "[AZa-z0-9]"
		if not match(pattern, username): 
			return False
		self.username = username
		return True

	def set_password(self, password:str) -> bool:
		pattern = "[AZa-z0-9]"
		if not match(pattern, password): 
			return False
		self.password = password
		return True



