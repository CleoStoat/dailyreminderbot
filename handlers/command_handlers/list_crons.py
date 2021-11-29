from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork
from handlers.utils import is_reply_to_msg
import config

def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    with uow:
        chat_id = update.effective_chat.id

        cron_msgs = uow.repo.list_cron_msgs(chat_id)

        
        if cron_msgs:
            text = "Crons in this chat:\n"
            text += "\n".join([f"c{cron_msg.cron_id}" for cron_msg in cron_msgs])
        else:
            text = "No crons in this chat."

        update.effective_message.reply_text(text=text, quote=True)
