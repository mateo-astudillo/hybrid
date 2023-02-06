from customtkinter import CTk
from View.login import Login


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Hybrid')
        self.geometry("350x450")


if __name__ == '__main__':
    app = App()
    login = Login(app)
    app.mainloop()

