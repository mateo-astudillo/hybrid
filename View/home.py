from customtkinter import CTk, CTkToplevel, CTkFrame, CTkLabel


class Home(CTk):
    def __init__(self):
        super().__init__()
        self.title('Home Page')
        self.geometry("1000x600+500+250")
        self.resizable(False, False)

        self.header = CTkFrame(master=self)
        self.header.pack(expand=True, fill="both")

        self.text = CTkLabel(master=self.header,
                             text="Logged successfull ✅", font=("Open Sans ExtraBold", 14))
        self.text.pack(expand=True)
        self.mainloop()


if __name__ == '__main__':
    pass
