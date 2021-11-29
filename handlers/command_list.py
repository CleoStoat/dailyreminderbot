from handlers.handler_model import CommandModel


COMMANDS = [
    CommandModel(
        priority=200,
        name="add_cron",
        description="Add a cron",
    ),
    CommandModel(
        priority=200,
        name="list_crons",
        description="Show the crons in this chat",
    ),
    CommandModel(
        priority=200,
        name="show_cron",
        description="Show the cron with specified cron id",
    ),
    CommandModel(
        priority=200,
        name="add_hours",
        description="Add hours to a cron",
    ),
    CommandModel(
        priority=200,
        name="del_hour",
        description="Add hours to a cron",
    ),
    CommandModel(
        priority=200,
        name="list_cron_hours",
        description="Add hours to a cron",
    ),
]
