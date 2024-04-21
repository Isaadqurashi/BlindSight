import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BlindSight")
        self.geometry("400x300")
        self.configure(background="#f0f0f0")

        background_image = Image.open("background.jpg")
        background_image = background_image.resize((1920, 1080), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        login_frame = tk.Frame(self, bg="#ffffff", bd=7)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        login_label = tk.Label(login_frame, text="Login", font=("Helvetica", 24), bg="#ffffff")
        login_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        username_label = tk.Label(login_frame, text="Username", bg="#ffffff")
        username_label.grid(row=1, column=0, padx=(10, 0))
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.grid(row=1, column=1, padx=(0, 10))

        password_label = tk.Label(login_frame, text="Password", bg="#ffffff")
        password_label.grid(row=2, column=0, padx=(10, 0))
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=(0, 10))

        login_button = ttk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Username:", username)
        print("Password:", password)
        
        self.withdraw()
        
        task_window = TaskAssignmentWindow(self)
        task_window.mainloop()

class TaskAssignmentWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("BlindSight")
        self.geometry("400x300")

        eeg_frame = ttk.Frame(self, padding="10")
        eeg_frame.pack(fill="both", expand=True)

        eeg_label = ttk.Label(eeg_frame, text="EEG Dataset:")
        eeg_label.grid(row=0, column=0, sticky="w")

        self.eeg_data_text = tk.Text(eeg_frame, width=40, height=10)
        self.eeg_data_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        eeg_button = ttk.Button(eeg_frame, text="Load EEG Data", command=self.load_eeg_data)
        eeg_button.grid(row=2, column=0, pady=(0, 10))

        task_frame = ttk.Frame(self, padding="10")
        task_frame.pack(fill="both", expand=True)

        task_label = ttk.Label(task_frame, text="Task Assignment:")
        task_label.grid(row=0, column=0, sticky="w")

        self.task_entry = ttk.Entry(task_frame, width=30)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)

        assign_button = ttk.Button(task_frame, text="Assign Task", command=self.assign_task)
        assign_button.grid(row=2, column=0, pady=(0, 10))

    def load_eeg_data(self):
        filename = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if filename:
            with open(filename, "r") as file:
                eeg_data = file.read()
            self.eeg_data_text.delete(1.0, "end")
            self.eeg_data_text.insert("end", eeg_data)

    def assign_task(self):
        task = self.task_entry.get()
        if task:
            print("Task Assigned:", task)

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
