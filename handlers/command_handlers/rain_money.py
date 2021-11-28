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

        user_ids = [user_info.user_id for user_info in uow.repo.list_user_infos()]
        ammount = random.randint(0, 1_000_000)

        uow.repo.increase_users_money(user_ids=user_ids, ammount=ammount)

        text = f"Everyone gained {ammount} money"
        update.effective_message.reply_text(text=text, quote=True)
        uow.commit()
