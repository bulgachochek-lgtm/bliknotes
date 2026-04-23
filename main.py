import logging
logging.basicConfig(level=logging.INFO)

print("TOKEN:", TOKEN)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """🎬 Оставьте заметку о фильме в таком формате:

1) Ваше имя или псевдоним
2) Название фильма
3) Оценка (1–5⭐️)
4) Текст вашей заметки
5) Ваш любимый фильм? (название, режиссер)

Ответы на вопросы направьте единым сообщением 👇
"""
    await update.message.reply_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    formatted = f"""🎬 Новая заметка

От: @{user.username}

{text}
"""

    # отправляем в чат редакции
    await context.bot.send_message(chat_id=-1003702231807, text=formatted)

    # отвечаем пользователю
    await update.message.reply_text("Спасибо! Мы получили вашу заметку 🎬 Чтобы отправить еще одну, напишите /start")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, handle_message))

app.run_polling()
