from datetime import date
from dataclasses import dataclass


@dataclass()
class Cron:
    chat_id: int
    message_id: int
    hour: int
    minute: int
    last_sent_on_date: date

@dataclass
class StaffMember:
    user_id: int
