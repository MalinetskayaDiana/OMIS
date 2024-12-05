# Admin_Window.py
import tkinter as tk
from tkinter import ttk

class AdminWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Admin Dashboard")
        self.geometry("800x600")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Обработчик закрытия окна

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Admin Dashboard", font=("Arial", 20)).pack(pady=20)

        self.table_frame = tk.Frame(self)
        self.table_frame.pack(pady=10)

        self.report_table = ttk.Treeview(self.table_frame, columns=("id", "title", "date", "manager_id"), show='headings')
        self.report_table.heading("id", text="Report ID")
        self.report_table.heading("title", text="Title")
        self.report_table.heading("date", text="Date")
        self.report_table.heading("manager_id", text="Manager ID")
        self.report_table.pack()

        # Пример данных отчетов
        example_reports = [
            {"id": 1, "title": "Quarterly Report", "date": "2023-01-15", "manager_id": "M001"},
        ]

        for report in example_reports:
            self.report_table.insert("", "end", values=(report["id"], report["title"], report["date"], report["manager_id"]))

        self.report_table.bind("<Double-1>", self.on_report_select)

        tk.Button(self, text="Employee Records", font=("Arial", 14), command=self.controller.show_employee_records).pack(pady=10)
        tk.Button(self, text="Logout", font=("Arial", 14), bg="red", command=self.controller.logout).pack(pady=20)

    def on_report_select(self, event):
        selected_item = self.report_table.selection()[0]
        report_id = self.report_table.item(selected_item, "values")[0]
        report_title = self.report_table.item(selected_item, "values")[1]
        report_body = "This is the body of the report."  # Добавьте логику для получения тела отчета
        self.controller.show_report_details(report_id, report_title, report_body)

    def on_closing(self):
        self.controller.on_closing()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminWindow(controller=None)
    app.mainloop()
