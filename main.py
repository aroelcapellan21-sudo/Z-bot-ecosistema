import os
from flask import Flask
from threading import Thread
import telebot

# 1. Servidor para que Render se ponga en "Live" (Verde)
app = Flask('')

@app.route('/')
def home():
    return "Ecosistema Z-Bot: Activo y Reportando."

def run():
    # Render usa el puerto 10000 por defecto
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. Tu Bot con el Token que ya conocemos
TOKEN = "7547012921:AAH8N_8F07i9XbW28D3m4T1h_W56N63M4pY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "✅ Ecosistema Reportando: Todo funciona correctamente. El sistema está estable y en línea.")

# 3. Función para ejecutar el servidor y el bot al mismo tiempo
def keep_alive():
    t = Thread(target=run)
    t.start()

if name == "main":
    keep_alive()
    print("Bot encendido y reportando...")
    bot.infinity_polling()
