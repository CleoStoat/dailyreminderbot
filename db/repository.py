from datetime import date
import decimal
from typing import List, Optional

from db.model import CronMessage, CronWeekday, CronHour, StaffMember
from sqlalchemy.orm import Session

class SqlAlchemyRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def add_cron(self,
        chat_id: int,
        message_id: int,
    ) -> int:
        cron = CronMessage(None, chat_id, message_id)
        self.session.add(cron)
        self.session.flush()
        return cron.cron_id

    def list_cron_msgs(self,
        chat_id: int,
    ) -> list[CronMessage]:
        cron_msgs = self.session.query(CronMessage).filter_by(chat_id=chat_id).all()
        self.session.flush()
        return cron_msgs

    def find_cron_msg_by_chat_id(self,
        chat_id: int,
        cron_id: int,
    ) -> Optional[CronMessage]:
        cron_msg = self.session.query(CronMessage).filter_by(chat_id=chat_id, cron_id=cron_id).first()
        return cron_msg

    def find_cron_msg(self,
        cron_id: int,
    ) -> Optional[CronMessage]:
        cron_msg = self.session.query(CronMessage).filter_by(cron_id=cron_id).first()
        return cron_msg

    def add_cron_hour(self,
        cron_id: int,
        hour: int,
        minute: int,
    ) -> None:
        cron_hour = CronHour(cron_id, hour, minute, date.min)
        self.session.add(cron_hour)
        return

    def find_cron_hour(self,
        cron_id: int,
        hour: int,
        minute: int,
    ) -> Optional[CronHour]:
        cron_hour = self.session.query(CronHour).filter_by(cron_id=cron_id, hour=hour, minute=minute).first()
        return cron_hour

    def del_cron_hour(self,
        cron_id: int,
        hour: int,
        minute: int,
    ) -> None:
        cron_hour = self.session.query(CronHour).filter_by(cron_id=cron_id, hour=hour, minute=minute).first()
        self.session.delete(cron_hour)

    def list_cron_hours(self,
        cron_id: int,
    ) -> list[CronHour]:
        cron_hours = self.session.query(CronHour).filter_by(cron_id=cron_id).all()
        return cron_hours

    def list_cron_hours_by_time(self,
        hour: int,
        minute: int,
    ) -> list[CronHour]:
        cron_hours = self.session.query(CronHour).filter_by(hour=hour, minute=minute).all()
        return cron_hours

    def del_cron(self,
        cron_id: int,
    ) -> None:
        cron_msg = self.session.query(CronMessage).filter_by(cron_id=cron_id).first()
        self.session.delete(cron_msg)
