from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Float,
)
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.sql.functions import user

from db.model import UserInfo, UserCode
import config

metadata = MetaData()

user_info = Table(
    "user_infos",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=False),
    Column("first_name", String),
    Column("last_name", String),
    Column("username", String),
    Column("money", Float),
    Column("last_updated", DateTime),
    Column("active", Boolean),
)

user_code = Table(
    "user_codes",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=False),
    Column("code", String, primary_key=True, autoincrement=False),
)

def start_mappers():
    mapper(UserInfo, user_info)
    mapper(UserCode, user_code)


def create_tables():
    engine = create_engine(config.get_sqlite_uri())
    metadata.create_all(engine)
