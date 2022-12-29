from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from properties import *

SQLALCHEMY_DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(
    DB_TYPE,
    DB_USER,
    DB_PASSWD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)

db_instance = Database(
    SQLALCHEMY_DATABASE_URL,
    min_size=5,
    max_size=1000,
    pool_recycle=500
    )

db_engine = create_engine(SQLALCHEMY_DATABASE_URL)
db_metadata = MetaData()

Base = declarative_base()