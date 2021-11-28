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
        if uow.repo.find_user_info(user_id) is None:
            user_info = UserInfo(
                user_id=user_id,
                first_name=update.effective_user.first_name,
                last_name=update.effective_user.last_name,
                username=update.effective_user.username,
                money=0.0,
                last_updated=datetime.now(),
                active=True,
            )
            uow.repo.add_user_info(user_info)


        random_code = 0
        while uow.repo.find_user_code(random_code) is not None:
            random_code = random.randint(0, 1_000_000)

        uow.repo.add_user_code(UserCode(user_id, random_code))

        text = f"Your new code: {random_code}"
        update.effective_message.reply_text(text=text, quote=True)
        uow.commit()
