import sys
import time

import telepot
from telepot.loop import MessageLoop

"""
$ python2.7 skeleton.py <token>
A skeleton for your telepot programs.
"""


def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)

    if flavor == 'chat':
        chat_id = msg['chat']['id']
        text = msg['text']
        tokens = text.split(" ")

        # Log
        if text.startswith('/'):
            pass
        elif chat_id in chatlogs.keys():
            chatlogs[chat_id] += [text,]
        else:
            chatlogs[chat_id] = [text,]

        if text == "/r/fiftyfifty":
            bot.sendMessage(chat_id, "50/50")
        elif text.startswith("/repeat"):
            n = int(tokens[1])
            bot.sendMessage(chat_id, "\n".join(chatlogs[chat_id][:n:-1]))

chatlogs = {}


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
