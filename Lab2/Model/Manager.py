from Admin import Admin

class Manager(Admin):
    def __init__(self, id, name, password, list_of_reports):
        super().__init__(id, name, password, role="Manager")
        self.list_of_reports = list_of_reports
