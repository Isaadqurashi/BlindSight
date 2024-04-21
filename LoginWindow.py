import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BlindSight")
        self.geometry("400x300")
        self.configure(background="#f0f0f0")

        # Load and display background image
        background_image = Image.open("background.jpg")
        background_image = background_image.resize((1920, 1080), Image.LANCZOS)  # or Image.BICUBIC
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        # Create login frame
        login_frame = tk.Frame(self, bg="#ffffff", bd=7)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login label
        login_label = tk.Label(login_frame, text="Login", font=("Helvetica", 24), bg="#ffffff")
        login_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Username entry
        username_label = tk.Label(login_frame, text="Username", bg="#ffffff")
        username_label.grid(row=1, column=0, padx=(10, 0))
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.grid(row=1, column=1, padx=(0, 10))

        # Password entry
        password_label = tk.Label(login_frame, text="Password", bg="#ffffff")
        password_label.grid(row=2, column=0, padx=(10, 0))
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=(0, 10))

        # Login button
        login_button = ttk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    def login(self):
        # Placeholder login function
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Username:", username)
        print("Password:", password)

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
