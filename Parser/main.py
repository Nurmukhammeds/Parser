import requests
from bs4 import BeautifulSoup


def parse(url, number):
    i = 1
    links = []
    while i <= number:
        r = requests.get(url+'page-'+str(i))
        soup = BeautifulSoup(r.content, 'html.parser')
        mydivs = soup.findAll("div", {"class": 'title-block tablet'})

        for div in mydivs:
            if div.a['href'] not in links:
                links.append('https://restolife.kz'+div.a['href'])
        i = i + 1
        

    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        header = soup.find("header", {"class": "main-heading"})
        kitchen = soup.find("div", {"class": "row"})
        str_test = header.a.text+' '+kitchen.text
        if 'Кухня:' in set(str_test.split()):
            print(link+' Кухня:',header.a.text,kitchen.text)




parse('https://restolife.kz/restoran/', 18)