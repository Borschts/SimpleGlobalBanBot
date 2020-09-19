from pyrogram import Client
from telegram import Bot
import time

import config


class MixedBot(Bot):

    def __init__(self, token, *args, **kwargs):
        super().__init__(token, *args, **kwargs)
        self.client: Client = Client(token, workdir="sessions")
        self.client.start()

    def kick(self, user_id):
        # 擊飛的部分
        for chat_id in config.groups:
            try:
                self.kick_chat_member(chat_id, user_id)
            except:
                print(f"無法從群組 {chat_id} 封鎖用戶 {user_id} ")
            time.sleep(1)
