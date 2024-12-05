# Manager_Window.py
import tkinter as tk

class ManagerWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Manager Dashboard")
        self.geometry("600x400")  # Увеличим размер окна
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Обработчик закрытия окна

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Manager Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="Employee Records", font=("Arial", 14), command=self.controller.show_employee_records).pack(pady=10)
        tk.Button(self, text="Create Report", font=("Arial", 14), bg="yellow", command=self.controller.show_report_window).pack(pady=10)
        tk.Button(self, text="Logout", font=("Arial", 14), bg="red", command=self.controller.logout).pack(pady=20)

    def on_closing(self):
        self.controller.on_closing()

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerWindow(controller=None)
    app.mainloop()
