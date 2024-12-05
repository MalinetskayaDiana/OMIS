from Model.DB import ReportDB
from Model.Report import Report

class ReportController:
    def __init__(self, report):
        self._report = report

    def add_report(self, report_id, title, body, date, manager_id):
        pass

    def find_report(self, number):
        pass
