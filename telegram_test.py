import argparse
from telegram.ext import Updater
def main(TOKEN):
    updater = Updater(TOKEN)
    chat_id = updater.chat_id
    message = "New commit done on the repo"
    updater.bot.send_mmessage(chat_id = chat_id, text = message)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type = str, required=True)
    args = parser.parse_args()
    if args.token:
        tk = str(args.token)
        print(tk)
        main(tk)
    else:
        print("NO TOKEN PROVIDED")
