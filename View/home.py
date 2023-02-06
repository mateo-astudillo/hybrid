from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.text = CTkLabel(master=self, text="Home", bg_color="blue", width=400)
		self.btn = CTkButton(master=self, text="hello")
		self.text.pack(padx=30, pady=30)


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	root.mainloop()
