from View import View
from Model import Model
from Controller import Controller


class App():
	def __init__(self):

		self.model = Model()
		self.view = View()
		self.controller = Controller(self.model, self.view)

		self.model.set_controller(self.controller)
		self.view.set_controller(self.controller)

		self.controller.run()


if __name__ == "__main__":
	App()
