import random
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.utils.helpers import escape_markdown

from db.unit_of_work import AbstractUnitOfWork

def inlinequery(update: Update, context: CallbackContext, uow: AbstractUnitOfWork) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Heads or tails",
            input_message_content=InputTextMessageContent(random.choice(["Heads", "Tails"])),
        ),
    ]

    update.inline_query.answer(results)
