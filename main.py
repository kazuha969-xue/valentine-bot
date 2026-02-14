import telebot

# MASUKKAN TOKEN BOT TELEGRAM KAMU DI SINI
TOKEN = "8585962237:AAHWI_wZltLXKYXRjONR61z4WXdMJPdId3E"

bot = telebot.TeleBot(TOKEN)

SPECIAL_DATE = "3-08-2025"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Kapan kita pacaran? 💕\n\nFormat: 3-08-2025"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.strip() == SPECIAL_DATE:
        bot.reply_to(
            message,
            "🎁 Happy Valentine ❤️\n\n"
            "Sejak 3 Agustus 2025 hidupku jadi lebih indah 💞\n"
            "Kamu itu bukan cuma spesial…\n"
            "kamu itu rumah buat aku 🏡💖\n\n"
            "Kalau disuruh pilih lagi,\n"
            "aku tetap pilih kamu.\n\n"
            "Jangan salting yaa 😆✨"
        )
    else:
        bot.reply_to(
            message,
            "Yahh salah 😜\nCoba ingat lagi tanggal spesial kita 💌"
        )

print("Bot is running...")
bot.infinity_polling(none_stop=True)
