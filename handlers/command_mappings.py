from handlers.command_handlers import help as help_cmd
from handlers.command_handlers import start
from handlers.command_handlers import settings
from handlers.command_handlers import new_code
from handlers.command_handlers import codes
from handlers.command_handlers import delete_code
from handlers.command_handlers import info
from handlers.command_handlers import toggle_active
from handlers.command_handlers import rain_money


COMMAND_MAPPINGS = {
    "help": help_cmd.cmd,
    "start": start.cmd,
    "settings": settings.cmd,
    "new_code": new_code.cmd,
    "codes": codes.cmd,
    "delete_code": delete_code.cmd,
    "info": info.cmd,
    "toggle_active": toggle_active.cmd,
    "rain_money": rain_money.cmd,
}
