# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize

word_tokenize("Can't wait", "[\w]+")

from nltk.tokenize import regexp_tokenize
regexp_tokenize("Can't wait", "[\s]+")
regexp_tokenize("Can't wait", "[\s]+", gaps=True)
