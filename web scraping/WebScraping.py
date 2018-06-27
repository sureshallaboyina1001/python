import requests
import bs4
result=requests.get("https://en.wikipedia.org/wiki/Room_641A")
soup=bs4.BeautifulSoup(result.text,'lxml')
soup.select('.mw-headline')
for item in soup.select('.mw-headline'):
    print(item.text)
