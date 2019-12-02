# cording: UTF-8

# モジュール参照を指定します。
# Slackbotライブラリ

from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('starting slackbot')
    main()