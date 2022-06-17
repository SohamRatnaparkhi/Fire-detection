import smtplib
import pywhatkit
from playsound import playsound
from datetime import datetime
from email.message import EmailMessage
import os
from twilio.rest import Client


def email_sender():
    sender = "manas.rathi21@vit.edu"
    reciever = "soham.ratnaparkhi@gmail.com"
    password = "12110626"
    msg_body = 'Fire detected by the model'

    msg = EmailMessage()
    msg['subject'] = msg_body
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)

        smtp.send_message(msg)


def whatsapp_sender():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    hrs, mn, sec = int(current_time.split(':')[0]), int(
        current_time.split(':')[1]), int(current_time.split(':')[2])
    phone_no = "+918999453973"
    message = "Fire detected by the model"
    pywhatkit.sendwhatmsg(phone_no, message, hrs, mn + 1)


def alarm_sound():
    playsound(r'MODEL\alarm.mp3')



import json

def send_sms(number,message):
    account_sid = os.environ['ACc62e408a5426258ac60abf4a917e43f2']
    auth_token = os.environ['8d44c6ebf82764d2b28de2029205d218']
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
             body='This is the ship that made the Kessel Run in fourteen parsecs?',
             from_='+12513253559',
             to='+919511959165'
         )
    
    print("sent....")


# send_sms("9511959165","Some message")
pass
