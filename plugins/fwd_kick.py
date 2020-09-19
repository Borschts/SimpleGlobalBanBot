from telegram import Update, Message
from telegram.ext import Dispatcher, CommandHandler

from mixed_bot import MixedBot
from utils.wrapper import admin


@admin
def ban(bot: MixedBot, update: Update):
    message: Message = update.effective_message
    reply_message: Message = message.reply_to_message

    if not reply_message:
        text = "請回覆一條訊息"
        message.reply_text(text)
        return

    user = reply_message.forward_from
    if not user:
        if reply_message.chat_id < 0:
            user = reply_message.from_user
        else:
            text = "請回覆想封鎖的目標的訊息（支持轉發）"
            message.reply_text(text)
            return

    text = f"正在封鎖 [user](tg://user?id={user.id})..."
    m: Message = message.reply_text(text, parse_mode="Markdown")

    bot.kick(user.id)
    m.edit_text("全域封鎖成功")


def register(dp: Dispatcher):
    dp.add_handler(CommandHandler("ban", ban))
