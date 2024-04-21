import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        ctk.set_default_color_theme("green")
        self.create_login_widgets()

    def create_login_widgets(self):
        ctk.CTkEntry(master=self, placeholder_text="Enter your email").pack(
            pady=10, padx=20
        )
        ctk.CTkEntry(master=self, placeholder_text="Enter your password").pack(
            pady=10, padx=20
        )
        ctk.CTkEntry(master=self, placeholder_text="Confirm your password").pack(
            pady=10, padx=20
        )
        ctk.CTkButton(master=self, text="Login", command=self.login_clicked).pack(
            pady=50, padx=20
        )

    def login_clicked(self):
        self.destroy()  # Close the login window
        # Open the second window with multiple options
        options_window = OptionsWindow()
        options_window.mainloop()





if __name__ == "__main__":
    app = App()
    app.mainloop()
