import os
from telegram.ext import ApplicationBuilder, CommandHandler

# Read token from Railway environment variable
TOKEN = os.getenv("8482347921:AAHPQ_R2k-fxbpd1Fq1PgtPE41QdouNSsL4")

async def start(update, context):
    await update.message.reply_text(
        "✅ Trader Bot is running!\n\n"
        "Bot is deployed successfully."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
