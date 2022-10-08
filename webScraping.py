from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com/"
# link = "https://www.google.com/search?q=trump&tbm=nws&sxsrf=ALiCzsah1FJR4Cm8iDhQkT0Rk_ZCqCk2Ug:1665120226714&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwiFhPycsM36AhVWTmwGHWb4AIMQpwV6BAgCEBY&biw=1536&bih=714&dpr=1.25"
link = "https://www.google.com/search?q=formula+1&rlz=1C1RXQR_enIN1015IN1015&biw=1365&bih=961&source=lnt&tbs=sbd%3A1%2Ccdr%3A1%2Ccd_min%3A1%2F1%2F2022%2Ccd_max%3A10%2F8%2F2022&tbm=nws"

def news(link):
    req = Request(link, headers = {'User-Agent':'Chrome/106.0.5249.103'})
    webpage = urlopen(req).read()

    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        # print(soup)
        for item in soup.find_all('div', attrs = {'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
            raw_link = (item.find('a', href = True)['href'])
            link = (raw_link.split('/url?q=')[1]).split('&sa=U&')[0]
            
            title = (item.find('div', attrs = {'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
            
            description = (item.find('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

            title = title.replace(',', '')
            description = description.replace(',', '')

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

            # document = open("data.csv", "a")
            # document.write('{}, {}, {}, {}\n'.format(title, time, descript, link))
            # document.close()
        next = soup.find('a', attrs = {'aria-label': 'Next page'})
        next = (next['href'])
        link = root + next
        news(link)

news(link)