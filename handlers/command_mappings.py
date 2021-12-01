from handlers.command_handlers import add_cron
from handlers.command_handlers import list_crons
from handlers.command_handlers import show_cron
from handlers.command_handlers import add_hours
from handlers.command_handlers import del_hour
from handlers.command_handlers import list_cron_hours
from handlers.command_handlers import del_cron


COMMAND_MAPPINGS = {
    "add_cron": add_cron.cmd,
    "list_crons": list_crons.cmd,
    "show_cron": show_cron.cmd,
    "add_hours": add_hours.cmd,
    "del_hour": del_hour.cmd,
    "list_cron_hours": list_cron_hours.cmd,
    "del_cron": del_cron.cmd,
}
