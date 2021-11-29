from datetime import timedelta
from functools import partial
import logging

from telegram.ext import Updater

import config
from helpers import init_db, set_handlers
from db.unit_of_work import SqlAlchemyUnitOfWork
from handlers.jobs.cronjob import cron_job

def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    init_db.init()

    updater = Updater(token=config.get_bot_token())
    uow = SqlAlchemyUnitOfWork()

    set_handlers.set_handlers(updater, uow)
    j = updater.job_queue
    callback = partial(cron_job, uow=uow)
    j.run_repeating(
        callback, 
        interval=timedelta(minutes=1), 
        first=0, 
        name="Checking crons to send",
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
