from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sql_app.database import db_metadata, db_engine

team = Table(
    "team",
    db_metadata,
    Column("team_id", Integer, primary_key=True, autoincrement=True),
    Column("team_name", String(20), nullable=False),
    Column("emp_fk", Integer, ForeignKey("employment.emp_id"), nullable=True)
)
# 테이블 정보로 테이블 생성한다
team.metadata.create_all(db_engine)
