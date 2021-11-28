from handlers.handler_model import MessageModel
from telegram.ext.filters import Filters


MESSAGES = [
    MessageModel(
        priority=300,
        name="hello",
        filters=Filters.regex("^[Hh]ello.?$")
    ),
    MessageModel(
        priority=300,
        name="goodbye",
        filters=Filters.regex("^[Gg]oodbye.?$")
    ),
]
