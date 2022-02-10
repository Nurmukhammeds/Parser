import requests
from bs4 import BeautifulSoup

url = 'https://restolife.kz'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
places = soup.find("div", {"class": "types-box"}).find("div", {"class": "inner-wrap"}).findAll("div", {"class": "row"})

#input1 = open('get_places.txt','w')

for place in places:
    for href in place.findAll("a", {"class": "item"}):
        try:
            page_number = 1
            try:
                parse = BeautifulSoup(requests.get(url+str(href['href'])).content, "html.parser")
                page = parse.find("div", {"class": "pages"}).findAll("a")[-1]
                page_number = page.text
            except:
                print('Error with page')


            print(url+str(href['href']), page_number)



        except:
            print("Error")







