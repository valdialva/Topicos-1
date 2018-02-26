# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger, NthOrderTagger
from nltk.corpus import brown

#1. Codigo para buscar palabras y frases espeficicas segun:
#Palabras etiquetadas como MD
MD = []
text = nltk.pos_tag(word_tokenize(state_union.raw()))
for word, pos in text:
    if pos == 'MD':
        MD.append(word)
print (sorted(MD))

#Identificar sustantivos plurales o verbos en tercera persona
for word, pos in text:
    if pos == 'VBZ' or pos == 'NNS':
        print (word, pos)

#Frases con la forma IN + DT + NN
for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(text):
        if (t1 == 'IN' and t2 == 'DT' and t3 == 'NN'):
            print(w1, w2, w3)

#Relacion de pronombres masculinos a femeninos
masc = len([w for (w,t) in text if w.lower() == "he"])
fem = len([w for (w,t) in text if w.lower() == "she"])
print ("masculino/femenino = ", (masc/fem))


#2. Encontrar texto taggeado en español
spanish_text = nltk.corpus.cess_esp.tagged_sents()
#Entrenar el texto con varios taggers
train_sents = spanish_text[:3000]
test_sents = spanish_text[3000:]
tagger1 = DefaultTagger('ncms000')
print ("Default ", tagger1.evaluate(test_sents))
tagger2 = UnigramTagger(train_sents)
print ("Unigram ", tagger2.evaluate(test_sents))
tagger3 = BigramTagger(train_sents)
print ("Bigram ", tagger3.evaluate(test_sents))
tagger4 = TrigramTagger(train_sents)
print ("Trigram ", tagger4.evaluate(test_sents))


'''
Basado en los resultados de los taggers usados en clase, se puede notar que
la precision es un poco mejor en espanol, lo cual puede ser debido al texto
usado o a la distinta estructura del idioma
'''

#3. Crear un tagger propio
#Define pattern
patterns = [
         (r'^-?[0-9]+$', 'CD'),             # cardinal numbers
         (r'.*', 'NN')                      # nouns (default)
]
 
NN_CD_Tagger = nltk.RegexpTagger(patterns)
UT = UnigramTagger()
NT = NgramTagger()