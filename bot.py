import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8592872461:AAF7F3_aJ5JXyZ817vIPLO-eieboj9S7SAQ"
bot = telebot.TeleBot(TOKEN)

CHANNEL_LINK_1 = "https://t.me/+1yE0qrc9kIlhNmJl"
CHANNEL_LINK_2 = "https://t.me/+Oi1XPw17o6tjNzM1"
CHANNEL_USERNAME_1 = "JKK_vlog"
CHANNEL_USERNAME_2 = "JKK_gaming"

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📢 Join 1", url=CHANNEL_LINK_1))
    markup.add(InlineKeyboardButton("⭐ Join 2", url=CHANNEL_LINK_2))
    markup.add(InlineKeyboardButton("Try Again ✅", callback_data="check_join"))

    bot.send_message(
        message.chat.id,
        "⚡🔥 *Jujutsu Kaisen Season 3 – Access Required* 🔥⚡\n\n"
        "🔓 Aage badhne ke liye dono channels join karo 👇\n"
        "✔ Only Updates • ✔ No Spam • ✔ Instant Alerts 🚀👻⚡",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):
    user_id = call.from_user.id

    try:
        member1 = bot.get_chat_member(f"@{CHANNEL_USERNAME_1}", user_id).status
        member2 = bot.get_chat_member(f"@{CHANNEL_USERNAME_2}", user_id).status

        if member1 in ["member","administrator","creator"] and member2 in ["member","administrator","creator"]:
            bot.edit_message_text(
                "🎌🔥 *Access Granted, Sorcerer!* 🔥🎌\n\n⚡ You are now inside the JJK Season 3 Bot ✔👻🚀⚡",
                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown"
            )
        else:
            bot.answer_callback_query(call.id, "❌ Pehle dono channels join karo!", show_alert=True)

    except Exception:
        bot.answer_callback_query(call.id, "⚠ Subscription check failed!", show_alert=True)

bot.infinity_polling()
