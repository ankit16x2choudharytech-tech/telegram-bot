# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, WEBSITE_LINK
from utils.helpers import get_welcome_text, get_link_text

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("English", callback_data="lang_en")],
        [InlineKeyboardButton("Hindi", callback_data="lang_hi")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(get_welcome_text(), reply_markup=reply_markup)

# Language selection button
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = "en" if query.data == "lang_en" else "hi"
    text = get_link_text(lang)

    keyboard = [
        [InlineKeyboardButton("Open Link", url=WEBSITE_LINK)],
        [InlineKeyboardButton("Generate Link Again 🔄", callback_data="regenerate")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text=text, reply_markup=reply_markup)

# Regenerate link button
async def regenerate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Detect language from previous message
    lang = "en" if "Your online service" in query.message.text else "hi"
    text = get_link_text(lang)

    keyboard = [
        [InlineKeyboardButton("Open Link", url=WEBSITE_LINK)],
        [InlineKeyboardButton("Generate Link Again 🔄", callback_data="regenerate")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern="lang_.*"))
    app.add_handler(CallbackQueryHandler(regenerate, pattern="regenerate"))

    print("Bot is running...")
    app.run_polling()