import os
import asyncio
from telegram.ext import Application, CommandHandler

async def start(update, context):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    
    link_personalizado = f"https://caixa-de-segredos.onrender.com/enviar/{user_id}"
    
    mensagem = (
        f"Olá, {first_name}! 🤫\n\n"
        f"Esta é a tua **Caixa de Segredos** anónima.\n"
        f"Copia o teu link exclusivo e envia para os teus amigos ou coloca no grupo:\n\n"
        f"{link_personalizado}\n\n"
        f"Todas as mensagens que te enviarem vão chegar aqui!"
    )
    
    await update.message.reply_text(mensagem, parse_mode="Markdown")

async def main():
    application = Application.builder().token("8914177691:AAFMZniiaOqZg0CxBum8VPXPOMgwgOAKS10").build()
    
    application.add_handler(CommandHandler("start", start))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
