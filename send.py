from telegram import Bot

# Your bot's token
token = '7907708312:AAH5dgEu7InL-nv1FG0xyK--adSkKQEj5sc'

# Initialize the bot
bot = Bot(token)

# User's chat_id (from the update)
chat_id = 720065938

# Send a message back
bot.send_message(chat_id=chat_id, text="Прикольна")
