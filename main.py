import telebot
import datetime
import time
import threading
import os

# Render ya tiene tu token guardado, aquí solo le decimos que lo use
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def reporte_guardia():
    while True:
        try:
            ahora = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"🕵️ Check de sistema: {ahora} - El Padre vigila.") 
            time.sleep(3600)
        except Exception as e:
            time.sleep(10)

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

if __name__ == "__main__":
    hilo_guardia = threading.Thread(target=reporte_guardia)
    hilo_guardia.daemon = True
    hilo_guardia.start()
    # Polling estable para que no se caiga en Render
    bot.polling(none_stop=True, interval=3, timeout=20)
    
