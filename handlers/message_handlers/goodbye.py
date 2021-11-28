from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork

def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    text = f"Goodbye {update.effective_user.full_name}"
    update.effective_message.reply_text(text=text, quote=True)
