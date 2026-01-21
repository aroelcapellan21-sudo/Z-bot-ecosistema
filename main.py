import telebot
import datetime
import time
import threading
import os

import telebot
import datetime
import time
import threading
import os

# 1. Usamos la "llave" (Token) de TU bot
TOKEN = os.environ.get("BOT_TOKEN", "7522511478:AAH_G5XvG_q3oG-7PCHX7XkC-m-R-TID298")
bot = telebot.TeleBot(TOKEN)

# 2. El Padre Vigilante (Vigilancia constante)
def reporte_guardia():
    while True:
        try:
            ahora = datetime.datetime.now().strftime('%H:%M:%S')
            # Esto se verá en los logs de Render que revisaste
            print(f"🕵️ Check de sistema: {ahora} - El Padre vigila.") 
            time.sleep(3600)
        except Exception as e:
            time.sleep(10)

# 3. Comando de Autoridad (Para darte tu ID y la hora)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    server_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    mensaje_respuesta = (
        f"¡Hola {user_name}!\n\n"
        f"🆔 Tu ID: {chat_id}\n"
        f"🕒 Hora Servidor: {server_time}\n"
        f"🛡️ El Padre está en control."
    )
    bot.reply_to(message, mensaje_respuesta)

# 4. Encendido blindado
if __name__ == "__main__":
    hilo_guardia = threading.Thread(target=reporte_guardia)
    hilo_guardia.daemon = True
    hilo_guardia.start()
    # Este polling evita que el bot se muera en la nube
    bot.polling(none_stop=True, interval=3, timeout=20)
    
