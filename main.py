import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Radar de Golos ONLINE!\n\nUsa /status para verificar."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHANNEL,
        text="📡 Radar de Golos está ATIVO e a monitorizar jogos!"
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("🤖 Bot iniciado com sucesso")

    app.run_polling()


if __name__ == "__main__":
    main()
