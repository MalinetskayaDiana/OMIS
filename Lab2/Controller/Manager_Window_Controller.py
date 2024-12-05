class ManagerController:
    def __init__(self, main_controller):
        self.main_controller = main_controller

    def show_employee_records(self):
        self.main_controller.show_employee_records()

    def show_report_window(self):
        self.main_controller.show_report_window()

    def logout(self):
        self.main_controller.logout()
