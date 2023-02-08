from customtkinter import CTkFrame, CTkLabel, CTkButton
from Controller import Controller

if __name__ == "__main__":
	from customtkinter import CTk


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		# Home page
		self.main_home = CTkFrame(master=self, width=300, height=300)
		# self.main_home_btn = CTkButton(
		# 	master=self.main_home,
		# 	command=self.toggle_menu_collapse,
		# 	text="Collapse"
		# )
		# self.main_home_btn.pack()
		self.home_label = CTkLabel(master=self.main_home, text="Home Page ", width=100, height=30)
		self.home_label.pack(padx=50)
		

		# Menu
		self.menu = CTkFrame(master=self)
		self.collapse = True
		self.menu_items = []
		self.menu_labels = []

		self.set_items()
		self.show_menu()
		
	def set_items(self):
		items = [
			("Menu", "🚗", self.toggle_menu_collapse),
			("Home", "🏠", None),
			("Stock", "🔎", None),
			("About", "A", None),
		]
		for name, icon, comm in items:
			self.create_menu_item(name, icon, comm)

	def set_controller(self, controller:Controller):
		self.controller = controller

	def show_menu_items(self):
		for item in self.menu_items:
			item.pack(padx=10, pady=10)

	def toggle_menu_collapse(self):
		if self.collapse:
			for label in self.menu_labels:
				label.pack(padx=10, pady=5, side="right")
		else: 
			for label in self.menu_labels:
				label.pack_forget()
		self.collapse = not self.collapse

	def create_menu_item(self, name:str, icon:str, comm):
		frm = CTkFrame(master=self.menu)
		i = CTkButton(master=frm, text=icon, command=comm, width=10)
		n = CTkButton(master=frm, text=name, command=comm)
		i.pack(padx=10, pady=5, side="left")
		self.menu_labels.append(n)
		self.menu_items.append(frm)
		
	def show_menu(self):
		self.menu.grid(row=0, column=0)
		self.main_home.grid(row=0, column=1)
		self.show_menu_items()


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	home.pack()
	root.mainloop()
