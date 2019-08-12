from nltk.corpus import state_union
import nltk
train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2005-GWBush.txt")

from nltk.tokenize import PunktSentenceTokenizer

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenised=custom_sent_tokenizer.tokenize(sample_text)

for i in tokenised:
    words=nltk.word_tokenize(i)
    tagged=nltk.pos_tag(words)
    chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    chunked.draw()

print(tagged)