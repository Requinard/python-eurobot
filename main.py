import sys
import time
from random import Random

import praw
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
            chatlogs[chat_id] += [text, ]
        else:
            chatlogs[chat_id] = [text, ]

        if text == "/fiftyfifty":
            bot.sendMessage(chat_id, "Fetching")
            reddit = get_reddit()
            for submission in reddit.subreddit('fiftyfifty').new(limit=10):
                print(submission.title)
                if Random().randint(0, 5) == 1:
                    bot.sendMessage(chat_id, "{0}: {1}".format(submission.title, submission.url),
                                    disable_web_page_preview=True)
        elif text == "/help" or text == "/start":
            bot.sendMessage(chat_id, """
            From the depths of hades we have retrieved ShibeBot
            
**Glossary**
- /save <n>; Save the last N messages to the eurosquad subreddit
- /fiftyfifty; Grab a random post from fiftyfifty
            """)
        elif text.startswith("/save"):
            n = int(tokens[1])
            if n is None or n > len(chatlogs[chat_id]):
                bot.sendMessage(chat_id, "Maybe try working me like I'm supposed to")
            else:
                saved_logs = chatlogs[chat_id][:n:-1]
                get_reddit().post
                bot.sendMessage(chat_id, "\n".join(saved_logs))


chatlogs = {}


def get_reddit():
    return praw.Reddit(
        client_id=sys.argv[2],
        client_secret=sys.argv[3],
        user_agent="Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
    )


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
