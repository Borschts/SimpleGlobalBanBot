from telegram import Update
from telegram.ext import Dispatcher, CommandHandler

from mixed_bot import MixedBot
from utils.wrapper import admin


@admin
def start(bot: MixedBot, update: Update):
    # 歡迎訊息
    text = "以下是全域封鎖的方式：\n\n" \
           "1. /nameban @username\n\n" \
           "2. 轉發一條訊息到管理群，並回覆該訊息使用 /ban 指令"
    update.effective_message.reply_text(text)


def register(dp: Dispatcher):
    dp.add_handler(CommandHandler("start", start))