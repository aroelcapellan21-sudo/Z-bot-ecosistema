import os
from flask import Flask
from threading import Thread
import telebot

app = Flask('')

@app.route('/')
def home():
    return "Z-Bot Vivo"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = "7547196020:AAFvjQ63B2C9v_78524Iu-8N68B8lH6M_9M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'socia'])
def send_welcome(message):
    bot.reply_to(message, "¡Z-Bot Despierta! Estoy activo y a tus órdenes, Yayo y Socia.")

if name == "main":
    keep_alive()
    print("Bot encendido correctamente...")
    bot.infinity_polling()
