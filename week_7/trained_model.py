import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics import confusion_matrix
import re


df_val=pd.read_csv('/home/admin1/twitter sentiment analysis/Twitter_Sentiment_Analysis/'
                                              'twitter-sentiment-analysis/train_E6oV3lV.csv')

list_val=pd.to_numeric(df_val['label'])
list_val=list(list_val)
df_val['label']=list_val

df_val['cleaned_tweet'] = df_val.tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))
df_val['cleaned_tweet'] = df_val.tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith('#')]))
df_val['cleaned_tweet'] = df_val.tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith(' ')]))


tweetVal_train,tweetVal_test,label_train,label_test=train_test_split(df_val['tweet'],df_val['label'],test_size=0.25)

cv = CountVectorizer()
vect = cv.fit(tweetVal_train)
tweetVal_train_vec = cv.transform(tweetVal_train)
# tweetVal_train
# print tweetVal_train_vec
# print 'tweetval_train',tweetVal_train
# print 'label_train',label_train

reg=LogisticRegression(random_state=0)
reg.fit(tweetVal_train_vec,label_train)
label_pred=reg.predict(vect.transform(tweetVal_test))
print("accuracy Score :",mt.accuracy_score(label_test,label_pred))
# print("Precisiopn Score:",mt.precision_score(label_test,label_pred))

# cm=confusion_matrix(label_test,label_pred)
# print(cm)

# # sample predection
# list_vect=["yes it is a value of famliuu"]
# print reg.predict(vect.transform(list_vect))


import pickle
pik_out=open('tweet_sentiment_analysis.pickle','wb')
pik_out2=open('tweet_sentiment_analysis_countVect.pickle','wb')

pickle.dump(reg,pik_out)
pickle.dump(cv,pik_out2)
pik_out.close()
pik_out2.close()


