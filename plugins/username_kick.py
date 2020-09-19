import time

from telegram import Update, Message
from telegram.ext import Dispatcher, CommandHandler

from mixed_bot import MixedBot
from utils.wrapper import admin


@admin
def namekick(bot: MixedBot, update: Update, args):

    client = bot.client
    message: Message = update.effective_message

    if not args:
        text = "需要指定一個Username"
        message.reply_text(text)
        return

    username = args[0]
    try:
        user = client.resolve_peer(username)
    except:
        text = f"找不到該用戶 {username}"
        message.reply_text(text)
        return

    text = f"正在封鎖 [user](tg://user?id={user.user_id})..."
    m = client.send_message(update.effective_chat.id, text, parse_mode="Markdown")

    time.sleep(0.5)
    bot.kick(user.user_id)
    text = f"全域封鎖成功"
    bot.edit_message_text(text, update.effective_chat.id, m.message_id)


def register(dp: Dispatcher):
    dp.add_handler(CommandHandler("nameban", namekick, pass_args=True))
