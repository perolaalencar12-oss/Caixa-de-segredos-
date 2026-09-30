import asyncio
from telegram.ext import Application

async def main():
    
    application = Application.builder().token("8914177691:AAFMZniiAoqZg0cXBum8VPXPOMGwgOAKS10").build()
    
  
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
