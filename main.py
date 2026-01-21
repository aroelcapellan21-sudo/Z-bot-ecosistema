import os, telebot
from flask import Flask
from threading import Thread

app = Flask('')

# Tu ID para reportes automáticos
CHAT_ID = "6578945006"

# Esta línea busca el secreto que guardaste en Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    # El bot te avisa cada vez que el Cron-job lo visita
    try:
        bot.send_message(CHAT_ID, "🦾 Reporte de Guardia: El Padre está vigilando el ecosistema.")
    except Exception as e:
        print(f"Error: {e}")
    return "Z-Bot Activo"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()

@bot.message_handler(commands=['start', 'socia'])
def welcome(message):
    bot.reply_to(message, "¡Z-Bot Blindado! Activo para Yayo y Socia.")

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
    
