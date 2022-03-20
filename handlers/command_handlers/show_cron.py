import json

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardMarkup


from db.unit_of_work import AbstractUnitOfWork
from handlers.utils import get_cron_id
import config


def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    with uow:
        if len(context.args) < 1:
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

        json_botones = json.loads(cron_msg.keybord_markup_json)
        rpm = InlineKeyboardMarkup.de_json(json_botones, context.bot)

        context.bot.copy_message(
            chat_id=chat_id,
            from_chat_id=config.get_store_chat_id(),
            message_id=cron_msg.message_id,
            reply_markup=rpm,
        )
