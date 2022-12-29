from datetime import datetime
from sqlalchemy import Table, Column, String, Integer, DateTime, ForeignKey
from sql_app.database import db_metadata, db_engine

emp = Table(
    "employment",
    db_metadata,
    Column("emp_id", Integer, primary_key=True, autoincrement=True),
    Column("emp_title", String(50), nullable=False),
    Column("register_date", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("dead_line", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("creer", Integer, nullable=False),
    Column("stack_fk", Integer, ForeignKey("stack.stack_id"), nullable=True)
)
emp.metadata.create_all(db_engine)
