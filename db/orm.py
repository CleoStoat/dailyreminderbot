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

from db.model import CronMessage, CronHour, CronWeekday, StaffMember
import config

metadata = MetaData()

cron_msg = Table(
    "cron_msgs",
    metadata,
    Column("cron_id", Integer, primary_key=True, autoincrement=True),
    Column("chat_id", Integer),
    Column("message_id", Integer),
    Column("keybord_markup_json", String(length=1500))
)

cron_hour = Table(
    "cron_hours",
    metadata,
    Column("cron_id", Integer, primary_key=True, autoincrement=False),
    Column("hour", Integer, primary_key=True, autoincrement=False),
    Column("minute", Integer, primary_key=True, autoincrement=False),
    Column("last_sent_on_date", Date),
)

cron_weekday = Table(
    "cron_weekday",
    metadata,
    Column("cron_id", Integer, primary_key=True, autoincrement=False),
    Column("weekday", Integer, primary_key=True),
)

staff_member = Table(
    "staff_members",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=False),
)

def start_mappers():
    mapper(CronMessage, cron_msg)
    mapper(CronHour, cron_hour)
    mapper(CronWeekday, cron_weekday)
    mapper(StaffMember, staff_member)


def create_tables():
    engine = create_engine(config.get_sqlite_uri())
    metadata.create_all(engine)
