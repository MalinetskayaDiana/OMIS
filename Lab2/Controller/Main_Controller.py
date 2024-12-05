# Main_Controller.py
import tkinter as tk
from View.Autorization_Window import AuthorizationWindow
from View.User_Window import UserWindow
from View.Manager_Window import ManagerWindow
from View.Admin_Window import AdminWindow
from View.Employee_Records_Window import EmployeeRecordWindow
from View.Report_Details_Window import ReportDetailWindow
from View.Create_Report_Window import ReportWindow

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.show_login_window()

    def show_login_window(self):
        self.login_window = AuthorizationWindow(self)
        self.login_window.mainloop()

    def show_user_window(self):
        self.user_window = UserWindow(master=self.root, controller=self)
        self.user_window.mainloop()

    def show_manager_window(self):
        self.manager_window = ManagerWindow(self)
        self.manager_window.mainloop()

    def show_admin_window(self):
        self.admin_window = AdminWindow(self)
        self.admin_window.mainloop()

    def show_employee_records(self):
        self.employee_record_window = EmployeeRecordWindow(self.root)
        self.employee_record_window.mainloop()

    def show_report_window(self):
        self.report_window = ReportWindow(self.root)
        self.report_window.mainloop()

    def show_report_details(self, report_id, report_title, report_body):
        self.report_details_window = ReportDetailWindow(self.root, report_id=report_id, report_title=report_title, report_body=report_body)
        self.report_details_window.mainloop()

    def login(self, login, password):
        if login == "user" and password == "user":
            self.login_window.destroy()
            self.show_user_window()
        elif login == "manager" and password == "manager":
            self.login_window.destroy()
            self.show_manager_window()
        elif login == "admin" and password == "admin":
            self.login_window.destroy()
            self.show_admin_window()
        else:
            tk.messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def logout(self):
        if hasattr(self, 'user_window') and self.user_window.winfo_exists():
            self.user_window.destroy()
        if hasattr(self, 'manager_window') and self.manager_window.winfo_exists():
            self.manager_window.destroy()
        if hasattr(self, 'admin_window') and self.admin_window.winfo_exists():
            self.admin_window.destroy()
        self.show_login_window()

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    app = MainController()
    app.root.mainloop()
