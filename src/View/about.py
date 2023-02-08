from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkTextbox
from PIL import Image

if __name__ == "__main__":
    from customtkinter import CTk, CTkTextbox
    PATH_LOGO = "../Assets/logo.jpg"
else:
    from Controller import Controller
    PATH_LOGO = "Assets/logo.jpg"


class About(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.controller = None
        self.configure(fg_color="black")
        self.widget_image()
        self.about_lbl = CTkLabel(
            master=self, text="About Us", font=("Open Sans ExtraBold", 17),)
        self.widget_textbox()

        self.widgets = [
            self.image,
            self.about_lbl,
            self.about_text,
        ]

        self.pack_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def get_text_info(self):
        with open("../../Static/info.txt", "r") as f:
            return f.read()

    def widget_textbox(self):
        about_info = self.get_text_info()
        self.about_text = CTkLabel(master=self)
        self.about_text.configure(
            text=about_info,
            fg_color="transparent",
            width=400,
            font=("Open Sans", 13),
            justify="center"
        )

    def widget_image(self):
        self.logo = CTkImage(dark_image=Image.open(PATH_LOGO), size=(300, 150))
        self.image = CTkLabel(
            master=self,
            image=self.logo,
            text="",
        )

    def pack_widgets(self):
        for w in self.widgets:
            w.pack(pady=5, padx=5)


if __name__ == "__main__":
    root = CTk()
    about = About(root)
    about.pack()
    root.mainloop()
