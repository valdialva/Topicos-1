#Alvaro Valdivieso
#Sebastian Ramos


import requests
from bs4 import BeautifulSoup

#Get web page 
req = requests.get('http://elmercioco.com/')
#Parse HTML
soup = BeautifulSoup(req.text, "html.parser")

#Get news from headlights
news  = soup.find_all('ul', ('class','article-block-big'))

#Get the links from the news selected
links = []

for link in news.find_all('a'):
    links.append(link.get('href'))

#Get the actual article links
articles = []

for article in links:
    articles.append(requests.get(article))
    
#Get the text from the news    
texts = []
for text in articles:
    texts.append(BeautifulSoup(text.text, "html.parser"))

#Get the titles
titles = []
for title in texts:
    titles.append(title.h1)
    
#Get the body of the news    
bodies = []
for body in texts:
    bodies.append(body.find_all('div', ('class','block-content')))
    
print {titles}
print (bodies)