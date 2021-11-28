from handlers.handler_model import CommandModel


COMMANDS = [
    CommandModel(
        priority=200,
        name="help",
        description="Get help",
    ),
    CommandModel(
        priority=200,
        name="start",
        description="Start the bot",
    ),
    CommandModel(
        priority=200,
        name="settings",
        description="Settings for this bot",
    ),
    CommandModel(
        priority=200,
        name="new_code",
        description="Get a random unique code",
    ),
    CommandModel(
        priority=200,
        name="codes",
        description="List of your codes",
    ),
    CommandModel(
        priority=200,
        name="delete_code",
        description="Delete a code you own",
    ),
    CommandModel(
        priority=200,
        name="info",
        description="Info about yourself",
    ),
    CommandModel(
        priority=200,
        name="toggle_active",
        description="Toggle between active and inactive",
    ),
    CommandModel(
        priority=200,
        name="rain_money",
        description="Make money rain from the skies",
    ),
]
