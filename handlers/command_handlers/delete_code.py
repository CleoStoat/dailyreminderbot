import random
from datetime import datetime
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from db.model import UserCode, UserInfo

from db.unit_of_work import AbstractUnitOfWork


def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    user_id = update.effective_user.id

    if len(context.args) < 1:
        text = "Please specify a code"
        update.effective_message.reply_text(text=text, quote=True)
        return

    code = context.args[0]

    with uow:
        user_code = uow.repo.find_user_code(code)
        
        if user_code is None:
            text = f"Code {code} doesn't exist"
            update.effective_message.reply_text(text=text, quote=True)
            return

        if user_code.user_id != user_id:
            text = f"You're not the owner of this code"
            update.effective_message.reply_text(text=text, quote=True)
            return

        uow.repo.delete_user_code(user_id, code)

        text = f"Successfully deleted code {code}"
        update.effective_message.reply_text(text=text, quote=True)

        uow.commit()
