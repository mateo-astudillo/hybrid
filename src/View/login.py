from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image

if __name__ == "__main__":
	from customtkinter import CTk


class Login(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		#! Image
		logo = CTkImage(
			dark_image = Image.open("Assets/logo.jpg"), size = (300, 150)
		)

		self.image = CTkLabel(
			master=self,
			image=logo,
			text="",
		)

		#! Entrys
		self.username_entry = CTkEntry(
			master=self,
			placeholder_text="Username",
		)

		self.password_entry = CTkEntry(
			master=self,
			show="*",
			placeholder_text="Password",
		)

		#! Buttons
		self.button_login = CTkButton(
			master=self,
			text="Login",
			text_color="black",
			fg_color="#C92C37",
			hover_color="#990510",
			font=("Open Sans ExtraBold", 14),
			width=180,
			command=self.check,
		)

		self.button_register = CTkButton(
			master=self,
			text="Register",
			text_color="#fff",
			fg_color="black",
			hover_color="#C92C37",
			font=("Open Sans Light", 14),
			width=50,
		)

		self.set_config()

		widgets = [
			self.image,
			self.username_entry,
			self.password_entry,
			self.button_login,
			self.button_register,
		]

		for widget in widgets:
			widget.pack(pady=15, ipadx=7)

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):

		self.configure(fg_color="black")

		for entry in [self.username_entry, self.password_entry]:
			entry.configure(
				corner_radius=27,
				width=180,
				border_width=0,
				placeholder_text_color="black",
				text_color="black",
				fg_color="#fff",
				justify="center",
				font=("Open Sans ExtraBold", 14),
			)

		for button in [self.button_login, self.button_register]:
			button.configure(
				corner_radius=27,
				border_width=0,
			)

	def check(self):
		self.controller.check( self.username_entry.get() )
		print(self.username_entry.get())
	


if __name__ == "__main__":
	root = CTk()
	login = Login(root)
	login.pack()
	root.mainloop()
