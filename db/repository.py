from datetime import date
import decimal
from typing import Optional

from db.model import Cron, StaffMember
from sqlalchemy.orm import Session

class SqlAlchemyRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def add_cron(self,
        chat_id: int,
        message_id: int,
        hour: int,
        minute: int,
        last_sent_on_date: date,
    ) -> None:
        ...

    def add_cron_hour(self, 
        chat_id: int,
        message_id: int,
        hour: int,
        minute:int,
    ) -> None:
        ...

    def del_cron(self, 
        chat_id: int,
        message_id: int,
    ) -> None:
        ...

    def del_cron_hour(self, 
        chat_id: int,
        message_id: int,
        hour: int,
        minute:int,
    ) -> None:
        ...
        
    def find_cron(self, 
        chat_id: int,
        message_id: int,
    ) -> Optional[Cron]:
        ...

    def list_cron(self, chat_id: int) -> list[Cron]:
        ...
        
    def list_cron_by_time(self, 
        chat_id: int, 
        hour: int, 
        minute: int
    ) -> list[Cron]:
        ...

    def list_cron_by_time_recent_unsent(self, 
        chat_id: int, 
        hour: int, 
        minute: int,
        recent_x_minutes: int,
        this_date: date
    ) -> list[Cron]:
        ...

    def update_cron_last_sent(self, 
        chat_id: int, 
        message_id: int, 
        last_sent_on_date: date
    ) -> None:
        ...
    
    def replace_cron_message(self, 
        chat_id: int, 
        message_id: int, 
        new_message_id: int, 
    ) -> None:
        ...

    def add_staff(self, user_id: int) -> None:
        ...

    def del_staff(self, user_id: int) -> None:
        ...
        
    def find_staff(self, user_id: int) -> Optional[StaffMember]:
        ...

    def list_staff(self) -> list[StaffMember]:
        ...



    def add_user_info(self, user_info: UserInfo) -> None:
        self.session.add(user_info)
        return
    
    def find_user_info(self, user_id: int) -> Optional[UserInfo]:
        user_info = self.session.query(UserInfo).get({"user_id":user_id})
        return user_info
    
    def add_user_code(self, user_code: UserCode) -> None:
        self.session.add(user_code)
        return

    def list_user_codes(self, user_id: int) -> list[int]:
        user_codes = self.session.query(UserCode).filter_by(user_id=user_id).all()
        return [user_code.code for user_code in user_codes]

    def delete_user_code(self, user_id: int, code: str) -> None:
        user_code = self.session.query(UserCode).get({"user_id":user_id, "code":code})
        if user_code is None:
            return
        self.session.delete(user_code)
        return
    
    def set_user_active(self, user_id: int, active: bool) -> None:
        user_info: Optional[UserInfo] = self.session.query(UserInfo).get({"user_id": user_id})
        if user_info is None:
            return
        user_info.active = active
        self.session.add(user_info)
        return
    
    def increase_users_money(self, user_ids: list[int], ammount: decimal.Decimal) -> None:
        self.session.query(UserInfo).filter(UserInfo.user_id.in_(user_ids)).update({UserInfo.money: UserInfo.money + ammount})
        return

    def update_user_info_last_updated(self, user_id: int, last_updated: datetime.datetime) -> None:
        user_info: Optional[UserInfo] = self.session.query(UserInfo).get({"user_id": user_id})
        if user_info is None:
            return
        user_info.last_updated = last_updated
        self.session.add(user_info)
        return

    def find_user_code(self, code: str) -> Optional[UserCode]:
        user_code = self.session.query(UserCode).filter_by(code=code).first()
        return user_code

    def list_user_infos(self) -> list[UserInfo]:
        user_infos = self.session.query(UserInfo).all()
        return user_infos