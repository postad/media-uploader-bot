import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    bot.reply_to(
        message,
        f"📸 file_id:\n<code>{file_id}</code>",
        parse_mode='HTML'
    )

@bot.message_handler(content_types=['video'])
def handle_video(message):
    file_id = message.video.file_id
    bot.reply_to(
        message,
        f"🎬 file_id:\n<code>{file_id}</code>",
        parse_mode='HTML'
    )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 ברוך הבא!\nשלח לי תמונה או וידאו,\nואחזיר לך את ה־<b>file_id</b> לשימוש בגוגל שיט.",
        parse_mode='HTML'
    )

print("🤖 Bot is running...")
bot.remove_webhook()
bot.infinity_polling()

