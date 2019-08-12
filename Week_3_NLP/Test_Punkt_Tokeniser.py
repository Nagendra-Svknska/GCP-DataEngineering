from nltk.corpus import gutenberg

print(dir(gutenberg))
print(gutenberg.fileids())

text = ""
for file_id in gutenberg.fileids():
    text += gutenberg.raw(file_id)

print(len(text))

from pprint import pprint
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True
trainer.train(text)

tokenizer = PunktSentenceTokenizer(trainer.get_params())

# Test the tokenizer on a piece of text
sentences = "Mr. James told me Dr. Brown is not available today. I will try tomorrow."

print("Test1 :",tokenizer.tokenize(sentences))
# ['Mr. James told me Dr.', 'Brown is not available today.', 'I will try tomorrow.']

# View the learned abbreviations
print("Test 1 abbrv:",tokenizer._params.abbrev_types)
# set([...])

# Here's how to debug every split decision
for decision in tokenizer.debug_decisions(sentences):
    pprint(decision)
    # print('=' * 30)


tokenizer._params.abbrev_types.add('dr')

print("Test 2:",tokenizer.tokenize(sentences))
# ['Mr. James told me Dr. Brown is not available today.', 'I will try tomorrow.']

for decision in tokenizer.debug_decisions(sentences):
    pprint(decision)
    # print
    # '=' * 30
