# bot.py
import requests

def send_message_to_telegram(chat_id, message):
    token = '7907708312:AAH5dgEu7InL-nv1FG0xyK--adSkKQEj5sc'  # Замените на ваш токен
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': 720065938,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message.")