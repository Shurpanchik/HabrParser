import urllib.request
from bs4 import BeautifulSoup

''' Поиск ссылок содержащее слово разарботка и вывод результатов в консоль '''
soup = BeautifulSoup(urllib.request.urlopen("https://habrahabr.ru/").read())


def print_actual_test_article():
    numberSite = int(1)
    text = ""
    while (True):
        try:
            ''' Поиск ссылок содержащее слово разарботка и вывод результатов в консоль '''
            url = "https://habrahabr.ru/page" + str(numberSite)
            print(url)
            soup = BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')

            for link in soup.find_all("article"):
                title = link.findNext("h2", {"class": "post__title"}).findNext("a", {"class": "post__title_link"})
                if str(title.contents[0]).__contains__("Разработка"):
                    text = text + "<br>" +  title.contents[0] + " " + title.get("href")

            numberSite = numberSite + 1
        except:
            break

    return text