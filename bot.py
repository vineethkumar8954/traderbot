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

# ---------------- COMMAND HANDLERS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Trader Bot is LIVE!\n\n"
        "📊 Upcoming features:\n"
        "• Candle close alerts\n"
        "• ML predictions\n"
        "• Win/Loss tracking\n\n"
        "Send /help to see commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Available Commands:\n\n"
        "/start – Bot status\n"
        "/ping – Test connection\n"
        "/help – Show help\n\n"
        "📷 You can also send chart screenshots."
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is running correctly.")

# ---------------- IMAGE HANDLER ----------------
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 Chart received.\n"
        "🔍 Candle analysis & ML prediction coming soon."
    )

# ---------------- WEBHOOK FIX ----------------
async def post_init(application):
    # VERY IMPORTANT: removes old webhook so polling works
    await application.bot.delete_webhook(drop_pending_updates=True)

# ---------------- MAIN ----------------
def main():
    if not TOKEN:
        raise RuntimeError("❌ BOT_TOKEN not found in environment variables")

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .post_init(post_init)   # <-- webhook fix
        .build()
    )

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))

    # Images
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    logging.info("🚀 Trader Bot started and polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
