from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
from googlesearch import search


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

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + ' /n')

    except sr.UnknownValueError:
        assistant(myCommand())

    except r.non_speaking_duration:
        exit()

    return command


def assistant(command):
    if 'open reddit' in command:
        chrome_path = '/usr/bin/firefox'
        url = 'https://www.reddit.com'
        webbrowser.get(chrome_path).open(url)

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
        recipient = myCommand()

        def contacts():
            # copy and paste module after talkToMe('Email Sent') and change friend to other contact name
            if 'friend' in recipient:
                content = input('Message(Do not press enter until message has finished): ')

                #init gmail SMTP
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                #identify to the Server
                mail.ehlo()
                #start the Encryption for session
                mail.starttls()
                #login
                mail.login(email_address, password)
                #change Person Name to Contact Full Name. Change recipient email address to the email address you are going to send the message to.
                #mail.sendmail('Person Name', 'recipient email address', content)
                #send message (duh)
                mail.sendmail('Arnab Chakraborty', 'arnab.chakraborty@thekaustschool.org', content)
                #close connection
                mail.close()

                talkToMe('Email Sent')

            if 'school friend' in recipient:
                content = raw_input('Message(Do not press enter until message has finished): ')

                #init gmail SMTP
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                #identify to the Server
                mail.ehlo()
                #start the Encryption for session
                mail.starttls()
                #login
                mail.login(email_address, password)
                #change Person Name to Contact Full Name. Change recipient email address to the email address you are going to send the message to.
                #mail.sendmail('Person Name', 'recipient email address', content)
                #send message (duh)
                mail.sendmail('John Kim', 'john.kim3.1415@gmail.com', content)
                #close connection
                mail.close()

                talkToMe('Email Sent')
            #Start your own contacts after this comment
        if recipient == contacts():
            contacts()


talkToMe('I am ready')

while True:
    assistant(myCommand())
