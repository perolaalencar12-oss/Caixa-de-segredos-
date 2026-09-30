import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        texto_recebido = update.message.text
        if TARGET_CHAT_ID:
            await context.bot.send_message(
                chat_id=TARGET_CHAT_ID,
                text=f"💌 **Nova mensagem anónima recebida:**\n\n{texto_recebido}"
            )
            await update.message.reply_text("O seu segredo foi enviado com sucesso de forma anónima!")
        else:
            await update.message.reply_text("O bot ainda não está totalmente configurado.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()















