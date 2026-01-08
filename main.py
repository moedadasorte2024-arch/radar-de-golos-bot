import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

bot = Bot(token=TOKEN)

bot.send_message(
    chat_id=CHANNEL,
    text="🤖 Radar de Golos está ONLINE ✅"
)
