from Model.DB import ManagerDB
from Model.Manager import Manager

class ManagerController:
    def __init__(self, manager):
        self._manager = manager

    def add_manager(self, id, name, password, list_of_reports):
        pass

    def find_manager(self, id):
        pass

    def create_report(self, number, title, body_of_report):
        pass