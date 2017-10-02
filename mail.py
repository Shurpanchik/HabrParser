# coding: utf-8

import smtplib
from email.mime.text import MIMEText

'''
    Метод отправки e-mail 
    toUser - получатель
    subj - тема письма
    text - содержание письма
'''
def sendMessage( toUser,subj,  text ):
    # отправитель
    fromUser = 'Shur1993@mail.ru'

    # SMTP-сервер
    server = "smtp.mail.ru"
    port = 25
    user_name = "yyyy@mail.ru"
    user_password = "xxxxxxxx"

    # формирование сообщения
    msg = MIMEText(text, "", "utf-8")
    msg['Subject'] = subj
    msg['From'] = fromUser
    msg['To'] = toUser

    # отправка
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user_name, user_password)
    s.sendmail(fromUser, toUser, msg.as_string())
    s.quit()