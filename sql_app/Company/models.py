from datetime import datetime
from sqlalchemy import Table, Column, String, Integer, DateTime, ForeignKey
from sql_app.database import db_metadata, db_engine, Base


class Company(Base):
    __tablename__ = 'company'
    company_id = Column("company_id",Integer,primary_key=True)
    company_name = Column("company_name",String(20), nullable=False)
    logo = Column("logo",String(50), nullable=True)
    location = Column("location",String(100), nullable=True)
    country = Column("country", String(50), nullable=True)
    emp_fk = Column("emp_fk", ForeignKey("employment.emp_id"), nullable=True)

company = Table(
    "company",
    db_metadata,
    Column("company_id", Integer, primary_key=True, autoincrement=True),
    Column("company_name", String(20), nullable=False),
    Column("logo", String(100), nullable=True),
    Column("location", String(100), nullable=True),
    Column("country", String(50), nullable=True),
    Column("emp_fk", Integer, ForeignKey("emp.emp_id"), nullable=True)
)
company.metadata.create_all(db_engine)
