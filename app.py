from customtkinter import CTk
from View.login import Login


class App(CTk):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.title('Login')
        self.resizable(False, False)
        self.geometry("350x530")
=======
        self.title('Hybrid')
        self.geometry("350x450")
>>>>>>> b17834391f8e82dbdc8d7a1d8030435ca788377f


if __name__ == '__main__':
    app = App()
<<<<<<< HEAD
    loginFrame = Login(app)
=======
    login = Login(app)
>>>>>>> b17834391f8e82dbdc8d7a1d8030435ca788377f
    app.mainloop()

