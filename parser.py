import urllib.request
from bs4 import BeautifulSoup

''' Поиск ссылок содержащее слово разарботка и вывод результатов в консоль '''
soup = BeautifulSoup(urllib.request.urlopen("https://habrahabr.ru/").read())


def print_actual_test_article():
    text = ""
    for link in  soup.find_all('a'):
        if  str(link.contents[0]).__contains__("Разработка"):
            text= text + "<br>"+ link.contents[0]+" "+link.get("href")
    #print(text)
    return text