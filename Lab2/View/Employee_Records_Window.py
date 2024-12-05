# Employee_Record_Window.py
import tkinter as tk
from tkinter import ttk

class EmployeeRecordWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Employee Records")
        self.geometry("800x400")  # Увеличим длину окна

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Employee Records", font=("Arial", 20)).pack(pady=20)

        self.table_frame = tk.Frame(self)
        self.table_frame.pack(pady=10)

        self.employee_table = ttk.Treeview(self.table_frame, columns=("id", "arrival_time", "departure_time", "work_time"), show='headings')
        self.employee_table.heading("id", text="Employee ID")
        self.employee_table.heading("arrival_time", text="Arrival Time")
        self.employee_table.heading("departure_time", text="Departure Time")
        self.employee_table.heading("work_time", text="Work Time")
        self.employee_table.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeRecordWindow(master=root)
    app.mainloop()
