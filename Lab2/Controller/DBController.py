from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database import Base, EmployeeDB, ManagerDB, AdminDB, ReportDB

class DatabaseController:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def open_session(self):
        self.session = self.Session()

    def close_session(self):
        if self.session:
            self.session.close()

    def add_employee(self, employee):
        pass

    def get_employee(self, employee_id):
        pass

    def add_manager(self, manager):
        pass

    def get_manager(self, manager_id):
        pass

    def add_admin(self, admin):
        pass

    def get_admin(self, admin_id):
        pass

    def add_report(self, report):
        pass

    def get_report(self, report_id):
        pass
