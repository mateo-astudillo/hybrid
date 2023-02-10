from customtkinter import CTkFrame,CTkLabel

if __name__ == "__main__":
    from customtkinter import CTk


class Filter(CTkFrame):
    def __init__(self,master = None):
        super().__init__(master)

        title = CTkLabel(master=self,text="Filter")
        title.pack(ipadx=40 ,ipady=80)

if __name__ == "__main__":
    root = CTk()
    filter = Filter(root)
    filter.pack()
    root.mainloop()