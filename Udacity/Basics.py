# summary
# normalize: lowercase, punctuations
# tokenize
# stop words
# stem / lemmatize

import requests
r = requests.get("https://news.ycombinator.com")
# print(r.text)

import re
pattern = re.compile(r'<.*?>')
# print(pattern.sub('', r.text))

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.get_text())

summaries = soup.find_all("tr", class_="athing")
# print(summaries)

summaries[0].find('a', class_="storylink").get_text().strip()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# print(stopwords.words('english'))

qttxt = "All that glitters is not gold. Hell is empty and all the devils are here. Now is the winter of our discontent. These violent delights have violent ends... The lady doth protest too much, methinks. Brevity is the soul of wit. Uneasy lies the head that wears a crown. Good night, good night! parting is such sweet sorrow, That I shall say good night till it be morrow. Fair is foul, and foul is fair: Hover through the fog and filthy air. Something is rotten in the state of Denmark."
wordtxt = word_tokenize(qttxt.lower())
stoppedtxt = [w for w in wordtxt if w not in stopwords.words('english')]
# print(stoppedtxt)

from nltk import pos_tag
sentence = word_tokenize(qttxt)
# pos_tag(sentence)


# named entity recognition
from nltk import ne_chunk
ne_chunk(pos_tag(word_tokenize("A simple sentence")))
# Err: The Ghostscript executable isn't found.

# stemming
from nltk.stem.porter import PorterStemmer
stemmed = [PorterStemmer().stem(w) for w in words]
# print(stemmed)

# lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
# print(lemmed)
lemmed = [WordNetLemmatizer().lemmatize(w, pos='v') for w in lemmed]
# print(lemmed)


