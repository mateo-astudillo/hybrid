from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
PATH_LOGO = os.getenv("PATH_LOGO")

class Login(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		logo = CTkImage( dark_image=Image.open(PATH_LOGO), size=(300, 150))
		self.widgets = {
			"image": CTkLabel(master=self, text = "",image=logo),
			"buttons": {
				"login": CTkButton(master=self, text="Login", command=self.login),
				"register": CTkButton(master=self, text="Register", command=self.register),
			},
			"entries":{
				"username": CTkEntry(master=self, placeholder_text="Username"),
				"password": CTkEntry(master=self, placeholder_text="Password", show="*")
			}
		}
		self.set_config()
		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		entries = self.widgets.get("entries")
		for entry in entries.values():
			entry.configure(
				corner_radius=27,
				border_width=0,
				placeholder_text_color="black",
				text_color="black",
				fg_color="#fff",
				justify="center",
				font=("Open Sans ExtraBold", 14),
			)

		buttons = self.widgets.get("buttons")
		for button in buttons.values():
			button.configure(
				corner_radius=27,
				border_width=0,#todo: revisar
			)

		buttons.get("login").configure(
			text_color = "black", #todo: revisar
			fg_color = "#C92C37",
			font = ("Open Sans ExtraBold", 14),
			hover_color = "#990510",
		)

		buttons.get("register").configure(
			text_color = "#fff",
			fg_color = "black",
			hover_color = "#C92C37",
			font = ("Open Sans Light", 14),
		)

	def pack_widgets(self):
		self.widgets.get("image").pack()
		entries = list(self.widgets.get("entries").values())
		buttons = list(self.widgets.get("buttons").values())

		for widget in entries + buttons:
			widget.pack(padx=7, pady=15, ipadx=20)




	def login(self):
		username = self.widgets.get("entries").get("username")
		password = self.widgets.get("entries").get("password")
		self.controller.login(username.get(), password.get())

	def register(self):
		pass


if __name__ == "__main__":
	root = CTk()
	login = Login(root)
	login.pack()
	root.mainloop()
