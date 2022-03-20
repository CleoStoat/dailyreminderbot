from datetime import date
from dataclasses import dataclass


@dataclass()
class CronMessage:
    cron_id: int
    chat_id: int
    message_id: int
    keybord_markup_json: str

@dataclass()
class CronHour:
    cron_id: int
    hour: int
    minute: int
    last_sent_on_date: date

@dataclass()
class CronWeekday:
    cron_id: int
    weekday: int

@dataclass
class StaffMember:
    user_id: int
