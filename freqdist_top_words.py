#!/usr/bin/env python
# coding=UTF-8
#
# Output the 50 most-used words from a text file, using NLTK FreqDist()
# (The text file must be in UTF-8 encoding.)
#
# Usage:
#
#   ./freqdist_top_words.py input.txt
#
# Sample output:
#
# et;8
# dolorem;5
# est;4
# aut;4
# sint;4
# dolor;4
# laborum;3
# ...
#
# Requires NLTK. Official installation docs: http://www.nltk.org/install.html
#
# I installed it on my Debian box like this:
#
# sudo apt-get install python-pip
# sudo pip install -U nltk
# python
# >>> import nltk
# >>> nltk.download('stopwords')
# >>> nltk.download('punkt')
# >>> exit()

import sys
import codecs
import nltk
from nltk.corpus import stopwords

# NLTK's default German stopwords
default_stopwords = set(nltk.corpus.stopwords.words('german'))

# We're adding some on our own - could be done inline like this...
# custom_stopwords = set((u'–', u'dass', u'mehr'))
# ... but let's read them from a file instead (one stopword per line, UTF-8)
stopwords_file = './stopwords.txt'
custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())

all_stopwords = default_stopwords | custom_stopwords

input_file = sys.argv[1]

fp = codecs.open(input_file, 'r', 'utf-8')

words = nltk.word_tokenize(fp.read())

# Remove single-character tokens (mostly punctuation)
words = [word for word in words if len(word) > 1]

# Remove numbers
words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
words = [word.lower() for word in words]

# Stemming words seems to make matters worse, disabled
# stemmer = nltk.stem.snowball.SnowballStemmer('german')
# words = [stemmer.stem(word) for word in words]

# Remove stopwords
words = [word for word in words if word not in all_stopwords]

# Calculate frequency distribution
fdist = nltk.FreqDist(words)

# Output top 50 words

for word, frequency in fdist.most_common(50):
    print(u'{};{}'.format(word, frequency))
