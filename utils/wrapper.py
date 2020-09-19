from telegram import Bot, Update, Message
from utils.memoize import MWT
import config
from pyrogram.api.types import InputPeerUser

@MWT(300)
def get_admin_ids(bot: Bot, chat_id):
    # 每五分鐘刷新群組的管理員UID
    return [a.user.id for a in bot.get_chat_administrators(chat_id)]

def is_admin(user_id, chat_id, bot):
    admins = get_admin_ids(bot, chat_id)
    return user_id in admins

def admin(func: callable):
    def wrapper(bot: Bot, update: Update, *args, **kwargs):
        if is_admin(update.effective_user.id, config.main_group, bot):
            return func(bot, update, *args, **kwargs)
        else:
            message: Message = update.effective_message
            message.delete()

    return wrapper
