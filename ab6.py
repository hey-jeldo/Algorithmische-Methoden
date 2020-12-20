import nltk
import HanTa
import matplotlib
from nltk.corpus import udhr

menschenrechte = udhr.words("German_Deutsch-Latin1")
menschenrechte_liste = list(menschenrechte)

standart_tagger = nltk.DefaultTagger("NN")

regechse = [(r'[A-Z][a-zßäöü]+','NN'),(r'[\wäöüß]+(isch|ich|at+|am|ind|nt|igt|ent|ig|bar|nd|iv|los|haft|izt|voll|är|al|el+|iert|ie?l|ös|ft|frei|fach|rt)','ADJA'),(r'[\wäöüß]+(e|l|r)n','VVINF'),(r'd[er|ie|as]{2}','ART')] # Eine Liste voller Tupel mit RegEx und Tags

re_tagger = nltk.RegexpTagger(regechse, backoff=standart_tagger)

menschenrechte_tagged = re_tagger.tag(menschenrechte)

root = '/Users/jeldo/Repositories/Algorithmische-Methoden/data/german_pos'
fileid = 'tiger.conll09'
columntypes = ['ignore', 'words', 'ignore', 'ignore', 'pos']
corp = nltk.corpus.ConllCorpusReader(root, fileid, columntypes, encoding='utf8')

german_ts = corp.tagged_sents()

# print(re_tagger.evaluate(german_ts))

from HanTa import HanoverTagger as ht
ht_tagger = ht.HanoverTagger('morphmodel_ger.pgz')

sample = "Definieren Sie eine Funktion pos_filter(), die den Hannover Tagger nutzt, um aus einem deutschsprachigen Text alle Token herauszufiltern, die einen bestimm- ten Tag zugewiesen bekommen haben. Achten Sie bitte darauf, dass der Text vor dem Taggen korrekt tokenisiert werden muss. Abend."

teggs = ['NN', 'VVINF', 'ADJA']

def pos_filter(text, tags):
    ergebnis = []
    for wort in nltk.word_tokenize(text):
        getestet = ht_tagger.analyze(wort)
        if getestet[1] in tags:
            ergebnis.append(getestet)
    return ergebnis



def pos_verteilung(text):
    fd = nltk.FreqDist([x[2] for x in ht_tagger.tag_sent(nltk.word_tokenize(text))])
    fd.plot()
    return fd

#pos_verteilung(sample)
