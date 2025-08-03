import telebot
import os

# קבלת הטוקן מה־Environment ב-Railway
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# תמונות
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    bot.reply_to(
        message,
        f"📸 file_id:<br><code>{file_id}</code>",
        parse_mode='HTML'
    )

# וידאו
@bot.message_handler(content_types=['video'])
def handle_video(message):
    file_id = message.video.file_id
    bot.reply_to(
        message,
        f"🎬 file_id:<br><code>{file_id}</code>",
        parse_mode='HTML'
    )

# התחלה
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 ברוך הבא! שלח לי תמונה או וידאו, ואני אחזיר לך את ה־<b>file_id</b> שתוכל לשים בגוגל שיט.",
        parse_mode='HTML'
    )

print("🤖 Bot is running...")
bot.infinity_polling()
