import os
from telegram.ext import ApplicationBuilder, CommandHandler

# Read token from Railway environment variable
TOKEN = os.getenv("8525684914:AAEMOqld7cRh03Azwwrg4YTjNfLHItV7zYE")

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
