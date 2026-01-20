import os
import telebot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Z-Bot Vivo"

def run():
    # Linea corta para que no se corte en tu celular
    p = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=p)

def keep_alive():
    Thread(target=run).start()

TOKEN = "7547196020:AAFvjQ63B2C9v_78524Iu-8N68B8lH6M_9M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'socia'])
def send_welcome(message):
    bot.reply_to(message, "¡Z-Bot Despierta! Activo para Yayo y Socia.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling(none_stop=True)
    
