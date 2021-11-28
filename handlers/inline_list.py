from telegram.ext.inlinequeryhandler import InlineQueryHandler
from handlers.inlinequery_handlers.heads_or_tails import inlinequery

INLINES = [
    InlineQueryHandler(callback=inlinequery)
]