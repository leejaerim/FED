from datetime import datetime
from sqlalchemy import Table, Column, String, Integer, DateTime, ForeignKey
from sql_app.database import db_metadata, db_engine, Base


class Emp(Base):
    __tablename__ = 'employment'
    emp_id = Column(Integer, primary_key=True)
    emp_title = Column(String(50), nullable=False)
    register_date = Column("register_date", DateTime(timezone=True), nullable=False, default=datetime.now)
    dead_line = Column("dead_line", DateTime(timezone=True), nullable=False, default=datetime.now)
    creer = Column("creer", Integer, nullable=False)
    company_fk = Column(Integer, ForeignKey("company.company_id"), nullable=True)


class EmpSk(Base):
    __tablename__ = 'emp_stack'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    emp_fk = Column("emp_fk", Integer, nullable=False)
    stack_fk = Column("stack_fk", Integer, nullable=False)


emp = Table(
    "employment",
    db_metadata,
    Column("emp_id", Integer, primary_key=True, autoincrement=True),
    Column("emp_title", String(50), nullable=False),
    Column("register_date", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("dead_line", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("creer", Integer, nullable=False),
    Column("stack_fk", Integer, ForeignKey("stack.stack_id"), nullable=True),
    #Column("company_fk", Integer, ForeignKey("company.company_id"), nullable=True)
)
emp_stack = Table(
    "emp_stack",
    db_metadata,
    Column("emp_fk", Integer),
    Column("stack_fk", Integer),
)
emp.metadata.create_all(db_engine)
emp_stack.metadata.create_all(db_engine)
