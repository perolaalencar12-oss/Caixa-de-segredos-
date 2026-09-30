import os
import asyncio
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler

app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Caixa de Segredos online!"

@app_web.route('/enviar/<user_id>')
def enviar_pagina(user_id):
    return f"Página de envio de segredos anónimos para o utilizador: {user_id}"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

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
    application = Application.builder().token("8914177691:AAFMZniiAoqZg0cXBuM8VPXPOMgwgOAKS10").build()
    application.add_handler(CommandHandler("start", start))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    asyncio.run(main())
