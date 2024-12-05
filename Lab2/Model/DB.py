from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class EmployeeDB(Base):
    pass

class ManagerDB(Base):
    pass

class AdminDB(Base):
    pass

class ReportDB(Base):
    pass
