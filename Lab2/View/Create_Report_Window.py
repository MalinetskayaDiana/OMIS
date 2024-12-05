# Report_Window.py
import tkinter as tk
from tkinter import messagebox

class ReportWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Creating Report")
        self.geometry("800x500")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Creating Report", font=("Arial", 20)).pack(pady=20)

        tk.Label(self, text="Title", font=("Arial", 14)).pack(anchor="w", padx=20)
        self.title_entry = tk.Entry(self, font=("Arial", 14), width=50)
        self.title_entry.pack(padx=20, pady=10)

        tk.Label(self, text="Body", font=("Arial", 14)).pack(anchor="w", padx=20)
        self.body_text = tk.Text(self, font=("Arial", 14), width=50, height=10)
        self.body_text.pack(padx=20, pady=10)

        tk.Button(self, text="Back", font=("Arial", 14), command=self.back).pack(side="left", padx=20, pady=20)
        tk.Button(self, text="Create Report", font=("Arial", 14), command=self.create_report).pack(side="right", padx=20, pady=20)

    def back(self):
        self.destroy()

    def create_report(self):
        title = self.title_entry.get()
        body = self.body_text.get("1.0", tk.END)
        if title and body.strip():
            messagebox.showinfo("Report Created", f"Report '{title}' created successfully!")
            self.destroy()
        else:
            messagebox.showwarning("Warning", "Please fill in both title and body fields.")
