import requests
from bs4 import BeautifulSoup

#Get web page 
req = requests.get('http://elmercioco.com/')
#Parse HTML
soup = BeautifulSoup(req.text, "html.parser")

#Get 
news  = soup.find_all('ul', ('class','article-block-big'))

links = []

for link in news.find_all('a'):
    links.append(link.get('href'))

articles = []

for article in links:
    articles.append(requests.get(article))
    
texts = []
for text in articles:
    texts.append(BeautifulSoup(text.text, "html.parser"))

titles = []
for title in texts:
    titles.append(title.h1)
    
bodys = []
for body in texts:
    bodys.append(body.find_all('div', ('class','block-content')))
    
#