import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class TaskAssignmentWindow(tk.Tk):
    def __init__(self):
        super().__init__()
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
    app = TaskAssignmentWindow()
    app.mainloop()
