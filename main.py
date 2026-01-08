import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHANNEL,
        text="🤖 Bot Radar de Golos iniciado com sucesso!"
    )

    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
