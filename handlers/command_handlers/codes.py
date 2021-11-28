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

    with uow:
        codes = uow.repo.list_user_codes(user_id)
        
        if len(codes) == 0:
            text = f"You have no codes."
            update.effective_message.reply_text(text=text, quote=True)
            return

        text = f"Here are your codes:\n"
        text += "\n".join(codes)
        update.effective_message.reply_text(text=text, quote=True)

        uow.commit()
