import schedule
import time

'''Запуск парсинга главной страницы хабра по расписанию'''


def start(job):
    #schedule.every().day.at("14:02").do(job)
    schedule.every(10).seconds.do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)