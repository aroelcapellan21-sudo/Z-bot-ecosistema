import os, telebot
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Z-Bot Activo"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()

# Esta línea busca el secreto que guardaste en Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'socia'])
def welcome(message):
    bot.reply_to(message, "¡Z-Bot Blindado! Activo para Yayo y Socia.")

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
    
