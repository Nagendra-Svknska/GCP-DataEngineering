import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_val='This is a bird with eye and beak where feathers are reddish-blue'
stop_words=stopwords.words('english')
print(type(stop_words))
final_val=[]
word_Tokens=word_tokenize(example_val)



for i in word_Tokens:
    if(i not in stop_words):
        final_val.append(i)
# final_val=[w in word_Tokens ]

print(final_val)