import Gwenda as gwenda
def to():
    if 'test' in gwenda.myCommand():
        'test' = 'arnab.chakraborty@thekaustschool.org'

def name():
    if 'test' in gwenda.myCommand():
        'test' = 'Arnab Chakraborty'

def email():
    print('What is your username?')
    email_address = raw_input('What is your email address?: ')
    print('What is your password?')
    password = raw_input('Password: ')
    talkToMe('Who is the recipient?')
    # init gmail SMTP
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    # identify to the Server
    mail.ehlo()
    # start the Encryption for session
    mail.starttls()
    # login
    mail.login(email_address, password)
    # change Person Name to Contact Full Name. Change recipient email address to the email address you are going to send the message to.
    # mail.sendmail('Person Name', 'recipient email address', content)
    # send message (duh)
    mail.sendmail(name(), to(), content)
    # close connection
    mail.close()

    gwenda.talkToMe('Email Sent')
def contacts():
    if 'test' in gwenda.myCommand():
     email()


