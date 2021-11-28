from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    Boolean,
    Float,
)
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import mapper

from db.model import Cron, StaffMember
import config

metadata = MetaData()

cron = Table(
    "crons",
    metadata,
    Column("chat_id", Integer, primary_key=True, autoincrement=False),
    Column("message_id", Integer, primary_key=True, autoincrement=False),
    Column("hour", Integer),
    Column("minute", Integer),
    Column("last_sent_on_date", Date),
)

staff_member = Table(
    "staff_members",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=False),
)

def start_mappers():
    mapper(StaffMember, staff_member)
    mapper(Cron, cron)


def create_tables():
    engine = create_engine(config.get_sqlite_uri())
    metadata.create_all(engine)
