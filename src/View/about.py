from customtkinter import CTkFrame, CTkLabel

if __name__ == "__main__":
    from customtkinter import CTk
else:
    from Controller import Controller


class About(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.controller = None
        self.lbl = CTkLabel(master=self, text="About Us").pack()

    def set_controller(self, controller):
        self.controller = controller


if __name__ == "__main__":
    root = CTk()
    about = About(root)
    about.pack()
    about.mainloop()
