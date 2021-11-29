from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork
from handlers.utils import is_reply_to_msg
import config

def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    with uow:
        reply_to_msg = is_reply_to_msg(update)
        if reply_to_msg is None:
            return

        # Copy message
        stored_msg_id = reply_to_msg.copy(chat_id=config.get_store_chat_id()).message_id

        # Add to database
        chat_id = update.effective_chat.id
        cron_id = uow.repo.add_cron(chat_id, stored_msg_id)

        text = "Added cron\n"
        text += f"cron_id: c{cron_id}\n"
        update.effective_message.reply_text(text=text, quote=True)
