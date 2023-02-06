from customtkinter import CTk
from View.view import View
from Model.model import Model
from Controller.controller import Controller

class App(CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("350x450")

        self.model = Model()
        self.view = View(self)
        self.controller = Controller(self.model, self.view)

        self.model.set_controller(self.controller)
        self.view.login.set_controller(self.controller)

        self.view.pack()
        self.view.login.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
