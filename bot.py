import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8376132800:AAEw2nQBrb_aZ9O-tpu9yJvcph1Fn1JZc_0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot is running\nUse /predict"
    )

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(0, 9)
    size = "BIG" if number >= 5 else "SMALL"
    await update.message.reply_text(
        f"🎯 Prediction\nBig / Small: {size}\nNumber: {number}"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
