import logging

from telegram.ext import Updater

from bot import mixed_bot
from plugins import register

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARNING)

updater = Updater(bot=mixed_bot)

register(updater.dispatcher)

updater.start_polling()
print("運行中...")
updater.idle()
