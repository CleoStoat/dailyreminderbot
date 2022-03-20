import json

from datetime import datetime
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardMarkup

from db.unit_of_work import AbstractUnitOfWork
from handlers.utils import is_reply_to_msg, get_cron_id
import config

def cron_job(
    context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    with uow:
        now = datetime.now()
        cron_hours = uow.repo.list_cron_hours_by_time(now.hour, now.minute)

        weekday = datetime.today().weekday()

        for cron_hour in cron_hours:
            cron_msg = uow.repo.find_cron_msg(cron_hour.cron_id)

            if cron_msg is None:
                continue

            rpm = None
            if cron_msg.keybord_markup_json:
                json_botones = json.loads(cron_msg.keybord_markup_json)
                rpm = InlineKeyboardMarkup.de_json(json_botones, context.bot)

            try:
                context.bot.copy_message(
                    chat_id=cron_msg.chat_id,
                    from_chat_id=config.get_store_chat_id(),
                    message_id=cron_msg.message_id,
                    reply_markup=rpm,
                )
            except Exception:
                continue
