from dotenv import load_dotenv
import telegram
from voice_recognizer import *
from bs4 import BeautifulSoup
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from gtts import gTTS
import requests
import re
import os
import cv2
import subprocess
import http.server
import socketserver
from os.path import join, dirname
from dotenv import load_dotenv
import ffmpeg
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

print('Ready?')

print("Bot is online!")


updater = Updater(os.environ.get('TOKEN'),use_context=True)

def sketch(update: Update,context:CallbackContext):
    os.system('rm pic.jpg')
    pic = context.bot.get_file(update.message.photo[-1].file_id)
    pic.download('pic.jpg')
    image = cv2.imread("pic.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imwrite('./draw.jpg',pencil_sketch)
    update.message.reply_photo(photo=open('draw.jpg', 'rb'))
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Please send me a voice message and I will speak to you!")
def draw(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Send me your image to sketch it!")
    updater.dispatcher.add_handler(MessageHandler(Filters.photo,sketch))


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""No need to worry just hold the mic and talk to me""")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Send me a voice message please")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Send me a voice message please")

# recieve voice
def voice(update: Update, context: CallbackContext):
    #save voice as mp3
    voice = update.message.voice
    voice.get_file().download('captured.ogg')
    # convert .ogg to .wav
    os.system('ffmpeg -i captured.ogg captured.wav -y')
    # send text
    text=get_text()
    print(text)
    result=str(run_alexa(text))
    print(result)
    # send audio
    if str(text).startswith('play') or str(text).startswith('sing') or 'sing' in str(text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.RECORD_VOICE)
        try:
            update.message.reply_audio(result)
        except:
            run_alexa("Sorry, I can't able to find the song you searched at the moment")
            update.message.reply_voice(open('captured.mp3', 'rb'))

    else:
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.RECORD_VOICE)
        tts = gTTS(result, lang='en-uk')
        tts.save('captured.mp3')
        try:
            update.message.reply_voice(open('captured.mp3', 'rb'))
        except:
            run_alexa("Sorry, Can you repeat again?")
            update.message.reply_voice(open('captured.mp3', 'rb'))
    




updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.voice, voice))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('draw', draw))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
 
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
#start http server on port 3000
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 3000
my_server = socketserver.TCPServer(("", PORT), handler_object)
print("Server started!")
# Star the server
my_server.serve_forever()
