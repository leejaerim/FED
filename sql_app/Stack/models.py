from sqlalchemy import Table, Column, String, Integer
from sql_app.database import db_metadata, db_engine

stack = Table(
    "stack",
    db_metadata,
    Column("stack_id", Integer, primary_key=True, autoincrement=True),
    Column("stack_name", String(20), nullable=False),
    Column("description", String(1000), nullable=False),
    Column("img", String(1000), nullable=False),
    Column("type", String(1), nullable=False),
)
# 테이블 정보로 테이블 생성한다
stack.metadata.create_all(db_engine)
