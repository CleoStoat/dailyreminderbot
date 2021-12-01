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


        cron_hours = uow.repo.list_cron_hours(cron_id)

        # Delete cascade cron hours
        for cron_hour in cron_hours:
            uow.repo.del_cron_hour(cron_id, cron_hour.hour, cron_hour.minute)

        # Delete the cron itself
        uow.repo.del_cron(cron_id)


        text = f"Deleted cron c{cron_id} and all of its hours\n"
        update.effective_message.reply_text(text=text, quote=True)
