# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union, brown
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger, RegexpTagger, NgramTagger


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
 
NN_CD_Tagger = RegexpTagger(patterns)

text = brown.tagged_sents()
train_sents = text[:3000]
test_sents = text[3000:]

# Construct and train the taggers
tagger1 = NgramTagger(2, train_sents)         # 1st order tagger
tagger2 = UnigramTagger(train_sents)           # 0th order tagger

#Evaluate taggers
print (tagger1.evaluate(test_sents))
print (tagger2.evaluate(test_sents))
print (NN_CD_Tagger.evaluate(test_sents))

# Combine the taggers
def backoff_tagger(train_sents, tagger_classes, backoff = None):  
    for cls in tagger_classes:    
        backoff = cls(train_sents, backoff = backoff)
    return backoff

tag1 = backoff_tagger(train_sents, [UnigramTagger, BigramTagger], backoff = NN_CD_Tagger)
print (tag1.evaluate(test_sents))
tag2 = backoff_tagger(train_sents, [UnigramTagger, TrigramTagger], backoff = NN_CD_Tagger)
print (tag2.evaluate(test_sents))
tag3 = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff = NN_CD_Tagger)
print (tag3.evaluate(test_sents))

#Repeat with different size
train_sents = text[:1000]
test_sents = text[1000:2000]

# Construct and train the taggers
tagger1 = NgramTagger(2, train_sents)         # 1st order tagger
tagger2 = UnigramTagger(train_sents)           # 0th order tagger

#Evaluate taggers
print (tagger1.evaluate(test_sents))
print (tagger2.evaluate(test_sents))
print (NN_CD_Tagger.evaluate(test_sents))

tag1 = backoff_tagger(train_sents, [UnigramTagger, BigramTagger], backoff = NN_CD_Tagger)
print (tag1.evaluate(test_sents))
tag2 = backoff_tagger(train_sents, [UnigramTagger, TrigramTagger], backoff = NN_CD_Tagger)
print (tag2.evaluate(test_sents))
tag3 = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], backoff = NN_CD_Tagger)
print (tag3.evaluate(test_sents))

'''
Con mas datos la precision aumenta en todos los taggers excepto en NN_CD_tagger
'''