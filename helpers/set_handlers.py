from functools import partial
from typing import Tuple

from telegram.botcommand import BotCommand
from telegram.botcommandscope import BotCommandScope
from telegram.ext import Updater, filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler

from db.unit_of_work import AbstractUnitOfWork
import config


from handlers.command_list import COMMANDS
from handlers.command_mappings import COMMAND_MAPPINGS
from command_overrides import OVERRIDES

def get_commands():
    for cmd in COMMANDS:
        cmd.callback = COMMAND_MAPPINGS[cmd.name]
        
        if cmd.name not in OVERRIDES:
            continue

        override = OVERRIDES[cmd.name]

        if "priority" in override:
            cmd.priority = override["priority"]

        if "name" in override:
            cmd.name = override["name"]

        if "priority" in override:
            cmd.priority = override["priority"]

        if "hidden" in override:
            cmd.hidden = override["hidden"]

    return COMMANDS

def set_bot_commands(
    updater: Updater, uow: AbstractUnitOfWork
) -> None:
    commands = get_commands()

    bot_commands: list[BotCommand | Tuple[str, str]] = []

    dispatcher = updater.dispatcher

    for cmd in commands:
        handler = CommandHandler(
                command=cmd.name,
                callback=partial(cmd.callback, uow=uow),
        )
        dispatcher.add_handler(handler, group=cmd.priority)
        

    bot_commands = [
        BotCommand(
                    command=cmd.name,
                    description=cmd.description,
        )
        for cmd in sorted(commands, key=lambda c: c.priority)
        if not cmd.hidden
    ]
    
    scope_type = config.get_command_scope()
    scope = None

    if scope_type:
        scope = BotCommandScope(type=scope_type)

    updater.bot.setMyCommands(commands=bot_commands, scope=scope)

def set_handlers(
    updater: Updater, uow: AbstractUnitOfWork
) -> None:
    set_bot_commands(updater, uow)
