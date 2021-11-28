import os
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "TOKEN": "token",
}

defaults = {
    "SQLITE_DB_NAME": "bot.db",
    "COMMAND_SCOPE": "",
}

defaults.update(credentials)

def get_env(env: str):
    result = os.getenv(env)
    if result is None:
        return defaults[env]
    return result

def get_sqlite_uri() -> str:
    dir = os.path.dirname(os.path.abspath(__file__))
    filename = get_env("SQLITE_DB_NAME")
    sqlite_db_path = os.path.join(dir + os.sep, filename)
    return f"sqlite:///{sqlite_db_path}"


def get_bot_token() -> str:
    return get_env("TOKEN")

def get_command_scope() -> str:
    return get_env("COMMAND_SCOPE")
