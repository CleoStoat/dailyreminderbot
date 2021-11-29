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

        hours = []
        for hour_str in context.args[1:]:
            hour = parse_hour(update, hour_str)
            if hour is None:
                return
            hours.append(hour)


        # Add to database

        added_hours = []
        already_existing_hours = []
        for hour, minute in hours:
            if uow.repo.find_cron_hour(cron_id, hour, minute) is not None:
                already_existing_hours.append(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}")
                continue

            added_hours.append(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}")
            uow.repo.add_cron_hour(cron_id, hour, minute)

        text = f"Added cron hours for c{cron_id}\n"

        if added_hours:
            for hour in added_hours:
                text += f"- {hour}\n"
        else:
            text += f"- No hours were added\n"

        if already_existing_hours:
            text += f"The following hours were already in the list:\n"
            for hour in already_existing_hours:
                text += f"- {hour}\n"

        update.effective_message.reply_text(text=text, quote=True)
