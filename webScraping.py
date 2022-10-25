from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

root = "https://www.google.com/"
# links_csv = pd.read_csv('/home/khal-drog0/Codes/Chatbot_News_Summarization/F1_News_Links.csv')
# links_list = links_csv.Link.tolist()

def news(link):
    req = Request(link, headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html5lib')
    print(soup)
    # for item in soup.find_all('div', attrs = {'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
    #     raw_link = (item.find('a', href = True)['href'])
    #     link = (raw_link.split('/url?q=')[1]).split('&sa=U&')[0]
            
    #     title = (item.find('div', attrs = {'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
            
    #     description = (item.find('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

    #     title = title.replace(',', '')
    #     description = description.replace(',', '')

    #     print(title)
    #     print(description)
    #     print(link)
    #     print()

    #     document = open("/home/khal-drog0/Codes/Chatbot_News_Summarization/data.csv", "a")
    #     document.write('{}, {}, {}\n'.format(title, description, link))
    #     document.close()
      
    # next = soup.find('a', attrs = {'aria-label': 'Next page'})
    # next = (next['href'])
    # link = root + next
    # try:
    #     news(link)
    # except:
    #     return

# for i in range(len(links_list)):
#     news(links_list[i])
#     i += 1

link = "https://www.google.com/search?q=formula+1&client=firefox-b-d&biw=1536&bih=703&sxsrf=ALiCzsa6Lr0_LgCAqDoiPXy_XgBhjPkk1Q%3A1665991134999&source=lnt&tbs=sbd%3A1%2Ccdr%3A1%2Ccd_min%3A10%2F17%2F2011%2Ccd_max%3A10%2F16%2F2012&tbm=nws"

news(link)