from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel, StringVar
from PIL import Image

class Login(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Login")

        #! Image
        logo = CTkImage(
            dark_image = Image.open("View/Assets/logo.jpg"), size=(300, 150)
            # dark_image=Image.open("Assets/logo.jpg"), size=(350, 150)
        )

        self.image = CTkLabel(
            master = self,
            image = logo,
            text = "", 
        )

        #! Entrys
        username_var = StringVar()
        password_var = StringVar()

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

        self.pack(expand=True, fill="both")

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
       

if __name__ == "__main__":
    root = CTk()
    root.geometry("350x530")
    root.resizable(width=False, height=False)
    login = Login(root)
    root.mainloop()
