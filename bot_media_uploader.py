import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    bot.reply_to(message, f"📸 file_id:\n`{file_id}`", parse_mode='Markdown')

@bot.message_handler(content_types=['video'])
def handle_video(message):
    file_id = message.video.file_id
    bot.reply_to(message, f"🎬 file_id:\n`{file_id}`", parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Send me a photo or video, and I’ll return the file_id for Google Sheet use.")

print("🤖 Bot is running...")
bot.infinity_polling()
