import os
import telebot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Z-Bot Blindado"

def run():
    puerto = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=puerto)

def keep_alive():
    Thread(target=run).start()

# Esta línea es la magia: busca el Token secreto en Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'socia'])
def welcome(message):
    bot.reply_to(message, "¡Z-Bot Blindado! Activo para Yayo y Socia.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling(none_stop=True)
    
