from apscheduler.schedulers.blocking import BlockingScheduler
""" Quickstart script for InstaPy usage """

# imports
import os
import sys
import random

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot
bot = Bot()
bot.login(username=os.environ['username'], password=os.environ['password'])
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=os.environ['hour'],minute=os.environ['minute'])
def scheduled_job():
    bot.unfollow_everyone()

sched.start()
