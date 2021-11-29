from typing import Optional, Tuple
from telegram.update import Update


def is_reply_to_msg(update: Update):
    reply_to_msg = update.effective_message.reply_to_message

    if reply_to_msg is None:
        text = "Error. No reply to message."
        update.effective_message.reply_text(text=text, quote=True)

    return reply_to_msg

def get_cron_id(update: Update, cron_code: str):
    if len(cron_code) < 1:
        text = "Error. Wrong cron id format."
        update.effective_message.reply_text(text=text, quote=True)
        return None

    if cron_code[0].lower() != "c":
        text = "Error. Wrong cron id format."
        update.effective_message.reply_text(text=text, quote=True)
        return None

    cron_id = cron_code[1:]

    if not cron_id.isnumeric():
        text = "Error. Wrong cron id format."
        update.effective_message.reply_text(text=text, quote=True)
        return None

    return int(cron_id)
    
def parse_hour(update: Update, hour_minute_str: str) -> Optional[Tuple[int, int]]:
    try:
        if "." in hour_minute_str:
            splitted = hour_minute_str.split(".")
            if len(splitted) != 2:
                raise ValueError()
            hour = int(splitted[0])
            minute = int(splitted[1])

        elif ":" in hour_minute_str:
            splitted = hour_minute_str.split(":")
            if len(splitted) != 2:
                raise ValueError()
            hour = int(splitted[0])
            minute = int(splitted[1])
        else:
            hour = int(hour_minute_str)
            minute = 0
        
        if not (0 <= hour <= 23):
            raise ValueError()

        if not (0 <= minute <= 59):
            raise ValueError()

        return hour, minute
    except Exception:
        text = f"Error. {hour_minute_str} doesn't have correct hour format"
        update.effective_message.reply_text(text=text, quote=True)
        return None


