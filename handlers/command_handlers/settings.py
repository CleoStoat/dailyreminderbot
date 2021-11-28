from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork


def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    text = f"This bot has no settings!"
    update.effective_message.reply_text(text=text, quote=True)
