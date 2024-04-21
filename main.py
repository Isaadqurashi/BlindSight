import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        ctk.set_default_color_theme("green")
        self.create_login_widgets()

    def create_login_widgets(self):
        ctk.CTkEntry(master=self, placeholder_text="Enter your email").pack(pady=10, padx=20)
        ctk.CTkEntry(master=self, placeholder_text="Enter your password").pack(pady=10, padx=20)
        ctk.CTkEntry(master=self, placeholder_text="Confirm your password").pack(pady=10, padx=20)
        ctk.CTkButton(master=self, text="Login", command=self.login_clicked).pack(pady=50, padx=20)

    def login_clicked(self):
        self.destroy()
        options_window = OptionsWindow()
        options_window.mainloop()

class OptionsWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("BlindSight")
        self.geometry("500x500")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        self.create_options_widgets()

    def create_options_widgets(self):
        ctk.CTkComboBox(master=self, values=["Caretaker 1", "Caretaker 2", "Caretaker 3"]).pack(pady=20, padx=20)
        ctk.CTkEntry(master=self, placeholder_text="Write your task").pack(pady=10, padx=20)
        ctk.CTkRadioButton(master=self, text="Confirm the option").pack(pady=10, padx=20)
        ctk.CTkSwitch(master=self, text="Get notification").pack(pady=10, padx=20)
        ctk.CTkButton(master=self, text="Send").pack(pady=10, padx=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
