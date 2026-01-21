import telebot
import datetime
import time
import threading
import os

# 1. Recuperamos la llave desde la configuración de Render
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 2. El Padre Vigilante
def reporte_guardia():
    while True:
        try:
            ahora = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"🕵️ Check de sistema: {ahora} - El Padre vigila.") 
            time.sleep(3600)
        except Exception as e:
            time.sleep(10)

# 3. Comando de Autoridad
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

# 4. Encendido estable
if __name__ == "__main__":
    hilo_guardia = threading.Thread(target=reporte_guardia)
    hilo_guardia.daemon = True
    hilo_guardia.start()
    bot.polling(none_stop=True, interval=3, timeout=20)
    
