import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

SPECIAL_DATE = "3-08-2025"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Kapan kita pacaran? 💕\nFormat: 3-08-2025")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == SPECIAL_DATE:
        bot.reply_to(message, "🎁 Ada hadiah buat kamu...")
        bot.reply_to(message,
        "Happy Valentine’s Day ❤️\n\n"
        "Sejak 3 Agustus 2025 hidupku lebih indah.\n"
        "Kalau disuruh pilih lagi, aku tetap pilih kamu 💞\n"
        "Jangan salting yaa 😆💖")
    else:
        bot.reply_to(message, "Yahh salah 😜 Coba ingat lagi tanggalnya!")

bot.infinity_polling()
