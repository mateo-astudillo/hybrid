from customtkinter import CTk
from View import View
from Model import Model
from Controller import Controller


class App(CTk):
	def __init__(self):
		super().__init__()

		self.model = Model()
		self.view = View(self)
		self.controller = Controller(self.model, self.view)

		self.model.set_controller(self.controller)
		self.view.login.set_controller(self.controller)
		self.view.home.set_controller(self.controller)

		self.view.pack()
		self.view.login.pack()


if __name__ == '__main__':
	app = App()
	app.mainloop()
