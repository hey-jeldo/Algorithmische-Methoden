import os
import re
import nltk
import matplotlib

ort_datum = "Trier, den 3.11.2020\nMit freundliche Grüßen"
result = re.search("((\d+)[./-](\d+)[./-](\d+))", ort_datum)
# [./-] hilft bei MM/DD/YY oder YYYY-MM-DD
date = result.group(1)
day = result.group(2)
month = result.group(3)
year = result.group(4)
print(f"Heute ist der {date}, oder ISO: {year}-{month}-{day}")
# gilt nur für DDMMYY(YY)

rhyme = '''
Betty bought a bit of butter, But the butter was so bitter,
So she bought some better butter, To make the bitter butter better.'''
print(re.findall("[Bb]\w+", rhyme))

emails = "test.acc+uni@g-mail.co.jp, notme@hey.com"
result = re.findall("(([\w\.\-]+)\+?[\w]*@([\w\-]+)(\.[\w]+\.?[\w]*))", emails)
for mail in result:
  print(mail)

text = "     Dieser,     Anblick   spottet;    jeder  Beschreibung,!   "
result = re.findall("([^\s,;]+)", text)
print(*result)

from nltk.corpus import PlaintextCorpusReader

corpus_dir = os.getcwd() + "/data"
corpus_texts = ".+\.txt"
mein_korpus = PlaintextCorpusReader(corpus_dir, corpus_texts, encoding='utf-8')
print(mein_korpus.fileids())

def stamm_erweiterung(wortstamm, liste):
    ergebnis = []
    for wort in liste:
        if wortstamm in wort:
            ergebnis.append(wort)
    return ergebnis

stamm_erweiterung("impf", mein_korpus.words('corona.txt'))

from nltk.corpus import stopwords

def stopwort_anzahl(text, sprache):
    treffer = []
    for wort in text:
        if wort in stopwords.words(sprache):
            treffer.append(wort)
    return len(treffer)

def test_lang(text):
    treffermenge = {}
    for sprache in stopwords.fileids():
        treffermenge[sprache] = stopwort_anzahl(text, sprache)
    sortiert = sorted(treffermenge, key=treffermenge.get)
    return sortiert[-1]

def sprach_identifikation(text):
    wb = {}
    if isinstance(text, nltk.corpus.reader.plaintext.PlaintextCorpusReader):
        for item in text.fileids():
            wb[item] = test_lang(mein_korpus.words(item))
        return wb
    return test_lang(text)

sprach_identifikation(mein_korpus.words('turk.txt'))
sprach_identifikation(mein_korpus)

def inhaltswoerter(text, sprache="german", anzahl=10):
    wb = {}
    if isinstance(text, nltk.corpus.reader.plaintext.PlaintextCorpusReader):
        for item in text.fileids():
            wb[item] = inhaltswoerter(mein_korpus.words(item))
        return wb
    textl = list(text)
    stopwort_liste = stopwords.words(sprache)
    stopworte_title = []
    for stopwort in stopwort_liste:
        stopworte_title.append(stopwort.title())
    stopwort_liste += stopworte_title
    stopwort_liste += [".", ",", "?", "!", "-", ";" , "–", '"', ":", "’", "„"]
    for stopwort in stopwort_liste:
        if stopwort in textl:
            while stopwort in textl:
                textl.remove(stopwort)
    fd = nltk.FreqDist(textl)
    tl = []
    for tuple in fd.most_common(anzahl):
        tl.append(tuple[0])
    return tl

inhaltswoerter(mein_korpus.words('corona.txt'))
inhaltswoerter(mein_korpus.words('biden-iraq.txt'), "english")
inhaltswoerter(mein_korpus.words('turk.txt'), "turkish" , 5)
inhaltswoerter(mein_korpus)
