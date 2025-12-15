import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ---------------- CONFIG ----------------
TOKEN = os.getenv("8525684914:AAEMOqld7cRh03Azwwrg4YTjNfLHItV7zYE")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ---------------- COMMANDS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Trader Bot is LIVE!\n\n"
        "📊 Features coming:\n"
        "• Candle close alerts\n"
        "• ML prediction\n"
        "• Win/Loss tracking\n\n"
        "Send /help to see commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Commands:\n\n"
        "/start – Check bot status\n"
        "/help – Show this help\n"
        "/ping – Test response\n\n"
        "📷 You will soon be able to send chart screenshots."
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is running fine.")

# ---------------- IMAGE HANDLER (PLACEHOLDER) ----------------
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 Chart received.\n"
        "🔍 Candle analysis + ML prediction coming soon."
    )

# ---------------- MAIN ----------------
def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN not found in environment variables")

    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))

    # Images (charts)
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    logging.info("🚀 Trader Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
