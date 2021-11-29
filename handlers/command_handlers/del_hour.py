from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork
from handlers.utils import get_cron_id, parse_hour
import config

def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    with uow:
        if len(context.args) < 2:
            text = "Error. Not enough args."
            update.effective_message.reply_text(text=text, quote=True)
            return
        
        cron_code = context.args[0]
        cron_id = get_cron_id(update, cron_code)
        if cron_id is None:
            return

        chat_id = update.effective_chat.id
        cron_msg = uow.repo.find_cron_msg_by_chat_id(chat_id, cron_id)

        if cron_msg is None:
            text = "Error. Couldn't find cron in this chat."
            update.effective_message.reply_text(text=text, quote=True)
            return

        hour = parse_hour(update, context.args[1])
        if hour is None:
            return

        hour, minute = hour
        hour_str = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"
        # Delete from database
        if uow.repo.find_cron_hour(cron_id, hour, minute) is None:
            text = f" Hour {hour_str} doesn't exist for cron c{cron_id}"
            update.effective_message.reply_text(text=text, quote=True)
            return

        uow.repo.del_cron_hour(cron_id, hour, minute)

        text = f"Deleted cron hour {hour_str} for c{cron_id}\n"
        update.effective_message.reply_text(text=text, quote=True)
