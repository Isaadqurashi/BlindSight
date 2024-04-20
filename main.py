import customtkinter as ctk
ctk.set_appearance_mode("System")


ctk.set_default_color_theme("green")



class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("BlindSight")
        self.geometry("500x500")
        ctk.CTkComboBox(master=self, values=["Caretaker 1", "Caretaker 2", "Caretaker 3"]).pack(
            pady=20, padx=20
        )
        ctk.CTkEntry(master=self, placeholder_text="write your task").pack(
            pady=20, padx=20
        )
        ctk.CTkRadioButton(master=self, text="Confirm the option").pack(pady=20, padx=20)
        ctk.CTkButton(master=self, text="send").pack(pady=20, padx=20)
        ctk.CTkSwitch(master=self, text="get notification").pack(pady=20, padx=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
