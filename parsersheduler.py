from  HabrParser import sheduler
from  HabrParser import  parser
from  HabrParser import mail

'''
    Скрипт отправки e-mail с актуальными статьями по разработке
'''

def send_news():
    mail.sendMessage("tshur@webzavod.ru", "Новости по разработке с сайта Хабр", parser.print_actual_test_article())
    print("Новости отправлены")


sheduler.start(send_news)