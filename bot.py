import asyncio
from telegram.ext import Application

async def main():
    # Inicializa o bot com o seu token do BotFather
    application = Application.builder().token("8914177691:AAFMZniiAoqZg0cXBum8VPXPOMGwgOAKS10").build()
    
    # Inicia o bot de forma assíncrona sem erros de event loop
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Mantém o bot ativo à escuta de mensagens
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
