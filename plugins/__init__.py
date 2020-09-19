from plugins import username_kick, fwd_kick, start
from telegram.ext import Dispatcher

def register(dp: Dispatcher):
    start.register(dp)
    username_kick.register(dp)
    fwd_kick.register(dp)