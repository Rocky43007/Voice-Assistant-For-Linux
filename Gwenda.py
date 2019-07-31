#Made by Arnab Chakraborty
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
from googlesearch import search
import Contacts as c




def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = r.recognize_google(audio)
        print("Gwenda thinks you said " + command)

    except sr.UnknownValueError:
        talkToMe('Sorry, I did not understand. Please repeat.')
        assistant(myCommand())


    return command


def assistant(command):
    if 'open reddit' in command:
        try:
            firefox_path = '/usr/bin/firefox'
            url = 'https://www.reddit.com'
            webbrowser.get(firefox_path).open(url)

    if 'test' in command:
        talkToMe('test')

    if 'bye' in command:
        talkToMe('Bye')
        exit()

    if 'Google' in command:
        talkToMe('Please repeat what you would like to search')
        query = myCommand()

        for j in search(query, tld="com", num=10, stop=1, pause=2):
            talkToMe('This is what I found on the internet:')
            print(j)

    if 'email' in command:
        print('What is your username?')
        email_address = raw_input('What is your email address?: ')
        print('What is your password?')
        password = raw_input('Password: ')
        talkToMe('Who is the recipient?')
        c.contacts()




talkToMe('I am ready')

while True:
    assistant(myCommand())
