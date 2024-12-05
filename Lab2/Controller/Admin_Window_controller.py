class AdminWindowController:
    def __init__(self, main_controller):
        self.main_controller = main_controller

    def show_employee_records(self):
        pass

    def show_report_details(self, report_id, report_title, report_body):
        pass

    def logout(self):
        self.main_controller.logout()
