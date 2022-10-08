from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com/"
# link = "https://www.google.com/search?q=trump&tbm=nws&sxsrf=ALiCzsah1FJR4Cm8iDhQkT0Rk_ZCqCk2Ug:1665120226714&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwiFhPycsM36AhVWTmwGHWb4AIMQpwV6BAgCEBY&biw=1536&bih=714&dpr=1.25"
link = "https://www.google.com/search?q=formula+1&tbs=qdr:m,sbd:1&tbm=nws&sxsrf=ALiCzsbQn5ChRntb0NDn6MOaN-tcKiHnYQ:1665210658144&source=lnt&sa=X&ved=2ahUKEwip1ISOgdD6AhUrRmwGHe8JAdIQpwV6BAgBECE&biw=1536&bih=714&dpr=1.25"

def news(link):
    req = Request(link, headers = {'User-Agent':'Chrome/106.0.5249.103'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html5lib')
    # print(soup)
    for item in soup.find_all('div', attrs = {'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
        raw_link = (item.find('a', href = True)['href'])
        link = (raw_link.split('/url?q=')[1]).split('&sa=U&')[0]
            
        title = (item.find('div', attrs = {'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
            
        description = (item.find('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

        title = title.replace(',', '')
        description = description.replace(',', '')

        time = ''
        descript = ''

        try:
            time = description.split('...')[1]
            descript = description.split('...')[0]
        except:
            pass

        print(title)
        print(time)
        print(descript)
        print(link)
        print()

        document = open("~/Codes/Chatbot_News_Summarization/data.csv", "a")
        document.write('{}, {}, {}, {}\n'.format(title, time, descript, link))
        document.close()
        
    next = soup.find('a', attrs = {'aria-label': 'Next page'})
    next = (next['href'])
    link = root + next
    news(link)

news(link)