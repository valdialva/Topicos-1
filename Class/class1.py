#importar libros de la libraria book
from nltk.book import *
#obtener informacion del texto 1
text1
#mostrat las primeras 100 palabras del texto 1
text1[:100]
#obtener el numero de palabras del texto
len(text1)
#obtener las palabras del texto sin repetidas
set(text1)
#numero de palabras del texto
len(set(text1))
#buscar una palabra dentro del contexto del texto
text1.concordance("timorous")
text1.concordance("monstrous")
#encontrar palabras similares - 
#a que se relaciona la palabra o que significa para el autor
text1.similar("monstrous")
#ver si 2 palabras son similares
'''
text2.concordande("monstrous")
text2.similar("monstrous")
'''
text2.common_contexts(["monstrous","very"])
#Encontrar la primera ocurrencia de una palabra en el texto
text1.index("more")

#las palabras mas recurrentes
v = FreqDist(text1)
print (v)
#Encontrar las 100 palabras mas usadas
print (v.most_common(100))
#plotear las 50 palabras mas significativas de acuerdo al uso
v.plot(50)
#plotear lo mismo en cumulativo
v.plot(50, cumulative=True)
#extraer el contexto de los textos de gutenberg
from nltk.corpus import gutenberg as gt
gt.fileids()
emma = gt.words('austen-emma.txt')
emma[0:100]
#obtener el promedio de repeticion de palabras
len(emma)/len(set(emma))
#para obtener el texto plano
gt.raw('austen-emma.txt')
#para obtenerlo por oraciones
gt.sents('austen-emma.txt')
#obtener la palabra de una oracion
gt.sents('austen-emma.txt')[100][2]

#get raw text
raw = gt.raw('blake-poems.txt')
raw[:100]
#get word list
tokens = gt.words("blake-poems.txt")
tokens[:100]
#get sentences
sents = gt.sents("blake-poems.txt")
sents[:1000]

#import brown corpues
from nltk.corpus import brown as br
#ver categorias de brown
br.categories()
br.fileids('news')

#import webtext
from nltk.corpus import webtext as wt
wt.fileids()
print (wt.fileids())

#import urllib to connect to internet
import urllib
#connect to a webpage
response = urllib.request.urlopen("http://www.gutenberg.org/cache/epub/56470/pg56470.txt")
#read the content of the page
raw = response.read().decode("utf8")
raw
len(raw)
raw[:1000]

#make the text tokenized to use with nltk
#import word_tokenizer
from nltk import word_tokenize
tokens = word_tokenize(raw)
tokens[:100]
#interprete the text with nltk
raw = nltk.Text(tokens)
raw.concordance("secret")

#extract news
response = urllib.request.urlopen("https://www.elcomercio.com/actualidad/cierredecampana-consultapopular-cuenca-quito-quininde.html")
noticia = response.read().decode("utf8")
noticia

from bs4 import BeautifulSoup

