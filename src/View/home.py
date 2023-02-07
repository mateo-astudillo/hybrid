from customtkinter import CTkFrame, CTkLabel, CTkButton
from time import sleep

if __name__ == "__main__":
	from customtkinter import CTk


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		# Home page
		self.main_home = CTkFrame(master=self)
		self.main_home.configure(width=300, height=300)
		self.main_home_btn = CTkButton(
			master=self.main_home,
			command=self.toggle_menu_collapse,
			text="Collapse"
		)
		self.main_home_btn.pack()
		

		# Menu
		self.menu = CTkFrame(master=self)
		self.collapse = False
		self.items = []
		self.menu_labels = []
		
		self.create_menu_item("Home", "🏠")
		self.create_menu_item("Stock", "🔎")
		self.create_menu_item("About", "A")

		self.show_menu()

	def set_controller(self, controller):
		self.controller = controller

	def show_menu_items(self):
		for i in self.items:
			i.pack(padx=10, pady=10)

	def toggle_menu_collapse(self):
		if self.collapse:
			self.show_menu_labels()
			self.collapse = False
		else: 
			self.hide_menu_labels()
			self.collapse = True

	def hide_menu_labels(self):
		for l in self.menu_labels:
			l.pack_forget()

	def show_menu_labels(self):
		for l in self.menu_labels:
			l.pack(padx=10, pady=5, side="right")

	def create_menu_item(self, name, icon):
		frm = CTkFrame(master=self.menu)
		i = CTkLabel(master=frm, text=icon)
		i.pack(padx=10, pady=5, side="left")
		n = CTkLabel(master=frm, text=name)
		n.pack(padx=10, pady=5, side="right")
		self.menu_labels.append(n)
		self.items.append(frm)

		
	def show_menu(self):
		self.menu.grid(row=0, column=0)
		self.main_home.grid(row=0, column=1)
		self.show_menu_items()


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	home.pack()
	root.mainloop()
