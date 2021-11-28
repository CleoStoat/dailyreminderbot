from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from db.unit_of_work import AbstractUnitOfWork
from handlers.command_list import COMMANDS

def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:

    text = "Avaliable commands:\n"
    text += "\n".join([f"/{cmd.name} - {cmd.description}" for cmd in COMMANDS if not cmd.hidden])

    update.effective_message.reply_text(text=text, quote=True)
