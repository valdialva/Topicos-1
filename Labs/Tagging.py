# -*- coding: utf-8 -*-
from nltk.corpus import state_union, treebank
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger

train_text = state_union.raw('1978-Carter.txt')
test_text = state_union.raw('1979-Carter.txt')

train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
tagger1 = DefaultTagger(train_sents)
tagger2 = UnigramTagger(train_sents, backoff=tagger1)
tagger3 = BigramTagger(train_sents, backoff=tagger2)
tagger4 = TrigramTagger(train_sents, backoff=tagger3)
tagger4.evaluate(test_sents)