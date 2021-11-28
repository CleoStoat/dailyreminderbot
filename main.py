import logging

from telegram.ext import Updater

import config
from helpers import init_db, set_handlers
from db.unit_of_work import SqlAlchemyUnitOfWork

def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    init_db.init()

    updater = Updater(token=config.get_bot_token())
    uow = SqlAlchemyUnitOfWork()

    set_handlers.set_handlers(updater, uow)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
