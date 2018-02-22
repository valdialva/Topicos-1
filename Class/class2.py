# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize

word_tokenize("Can't wait", "[\w]+")

from nltk.tokenize import regexp_tokenize
regexp_tokenize("Can't wait", "[\s]+")
regexp_tokenize("Can't wait", "[\s]+", gaps=True)

s = "I was watching TV"
tagged = nltk.pos_tag(word_tokenize(s))
allnoun = [word for word, pos in tagged if pos in ['NN', 'NNP']]

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text = state_union.raw('1978-Carter.txt')
test_text = state_union.raw('1979-Carter.txt')
sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = sent_tokenizer.tokenize(test_text)
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print (tagged)
        
    except Exception as e:
        print (str(e))
        
process_content()

from nltk.tag import DefaultTagger
tagger = DefaultTagger('NN')
tagger.tag(['Hello', 'World'])

from nltk.corpus import treebank
test_sents = treebank.tagged_sents()[3000:]
tagger.evaluate(test_sents)
tagger.tag_sents([['Hello', 'world', '.', 'How', 'are', 'you', '?']])

from nltk import untag
untag([('Hello', 'NN'), ('World', 'NN')])

from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents)
treebank.sents()[0]
tagger.tag(treebank.sents()[0])
tagger.evaluate(test_sents)

from nltk.tag import DefaultTagger, UnigramTagger
tagger1 = DefaultTagger('NN')
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
tagger2 = UnigramTagger(train_sents, backoff=tagger1)
tagger2.evaluate(test_sents)

import pickle
f = open('tagger.pickle', 'wb')
pickle.dump(tagger, f)
f.close()
f = open('tagger.pickle', 'rb')
tagger = pickle.load(f)

#See if biggram tagger has more or less precition than unigram tagger
from nltk.tag import BigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
BG_tagger = BigramTagger(train_sents)
treebank.sents()[0]
BG_tagger.tag(treebank.sents()[0])
BG_tagger.evaluate(test_sents)


#See if Trrigram tagger has more or less precition than unigram tagger
from nltk.tag import TrigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
TG_tagger = TrigramTagger(train_sents)
treebank.sents()[0]
TG_tagger.tag(treebank.sents()[0])
TG_tagger.evaluate(test_sents)

#combine 3 taggers
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
tagger1 = DefaultTagger(train_sents)
tagger2 = UnigramTagger(train_sents, backoff=tagger1)
tagger3 = BigramTagger(train_sents, backoff=tagger2)
tagger4 = TrigramTagger(train_sents, backoff=tagger3)
tagger4.evaluate(test_sents)
