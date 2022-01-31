import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser
from plugins import time
from plugins import hello
from plugins import voice_api
from plugins import search
from plugins import music

listener = sr.Recognizer()




def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                print(command)
                command = command.replace('hello', '')
                return command
            else:
                command = "sorry"
                print(command)
                return command
    except:
        command = 'sorry'
        return command


def get_text():
    try:
        with sr.AudioFile('captured.wav') as source:
            # listen for the data (load audio to memory)
            audio_data = listener.record(source)
            # recognize (convert from speech to text)
            text = listener.recognize_google(audio_data)
            print(text)
            return text
    except:
        return "Sorry, Please say that again!"


def run_alexa(text):
    command = text
    print(command)
    if str(command).startswith('play') or str(command).startswith('sing') or 'sing' in str(command):
        song = command.replace('play', '')
        print(music.fetch(song))
        return music.fetch(song)
    elif 'time' in command:
        return time.plugin_time()
    elif 'what is your name' in command:
        return "My name is NodeSpeech Bot"
    elif 'hello' in command:
        return hello.hello()
    else:
        return voice_api.voiceApi(command)
    