#Alvaro Valdivieso
#Sebastian Ramos


import requests
from bs4 import BeautifulSoup

#First page ----------------------------------------------------------
#Get web page 
req = requests.get('http://elmercioco.com/')
#Parse HTML
soup = BeautifulSoup(req.text, "html.parser")

#Get news from headlights
news  = soup.find_all('ul', ('class','article-block-big'))

#Get the links from the news selected
links = []

for link in news[0].find_all('a'):
    links.append(link.get('href'))

links = set(links)

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
    titles.append(title.h1.get_text())
    
#Get the body of the news    
bodies = []
for body in texts:
    bodies.append(body.find_all('div', ('class','block-content'))[0].find_all('p'))

#Extract only the text
p_filter = []
for text in bodies:
    temp = ''
    for p in text:
        temp+= p.text
    p_filter.append(temp)

#Print the news
for i in range(0, len(titles)):
    print (i+1)
    print (titles[i] + p_filter[i])


#Second page ---------------------------------------------------------
#Get web page 
req = requests.get('https://www.theonion.com/')
#Parse HTML
soup = BeautifulSoup(req.text, "html.parser")

#Get news from headlights
news  = soup.find_all('div', ('class','featured-items js_zone-items'))

#Get the links from the news selected
links = []

for link in news[0].find_all('a'):
    links.append(link.get('href'))

links = set(links)

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
    titles.append(title.find_all('h1', ('class','headline hover-highlight entry-title js_entry-title'))[0].a.text)
    
#Get the body of the news    
bodies = []
for body in texts:
    bodies.append(body.find_all('div', ('class','post-content entry-content js_entry-content '))[0].find_all('p'))

#Extract only the text
p_filter = []
for text in bodies:
    temp = ''
    for p in text:
        temp+= p.text
    p_filter.append(temp)
    
#Print the news
for i in range(0, len(titles)):
    print (i+1)
    print (titles[i] + '\n' + p_filter[i])
