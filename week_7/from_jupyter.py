#!/usr/bin/env python
# coding: utf-8

# To detect negative speech in tweets.
#
# ## Dataset :
# The data set contains tweets and sentiment related to it. Her ewe need to predict the sentiment for a given tweet.
# Here, in label
# * __0  --> Negative Tweet__
# * __1  --> Regulat Tweet__

# ## Step 1 : Import libraries
#
# Here we are gonna use NLTK, i.e., Natural Language Tool Kit
# As name suggests, it is contains all the modules required for NLP operations.
# In this problem, as we are dealing with statements, NLTK suits well.

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from wordcloud import WordCloud,STOPWORDS
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.pipeline import make_pipeline

import warnings
warnings.filterwarnings("ignore")
import pickle


# ## Step 2: Import datasets

# In[15]:


train  = pd.read_csv("/home/admin1/twitter sentiment analysis/Twitter_Sentiment_Analysis/"
                     "twitter-sentiment-analysis/train_E6oV3lV.csv")
test = pd.read_csv("/home/admin1/twitter sentiment analysis/Twitter_Sentiment_Analysis/twitter-sentiment-analysis/test_tweets_anuFYb8.csv")
train.sample(2)
print train

# In[16]:


train.shape, test.shape
print "Test Print :",train.shape, test.shape


# ## Step 3 : Data cleaning and Preprocessing

# Combine train and test dataset for pre processing. Here we'll remove all the unnecessary contents from the data. This will help to increase the accuracy.

# In[17]:


df = train.append(test, ignore_index = True)
df.shape


# Remove twitter handlers i.e., @user

# In[18]:

print train.info()
train['cleaned_tweet'] = train.tweet.apply(lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))
test['cleaned_tweet'] = test.tweet.apply(lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))




# ### Hashtags
# Graph to show normal tweets

# In[19]:


#Select all words from normal tweet
normal_words = ' '.join([word for word in train['cleaned_tweet'][train['label'] == 0]])
#Collect all hashtags
pos_htag = [htag for htag in normal_words.split() if htag.startswith('#')]
#Remove hashtag symbol (#)
pos_htag = [pos_htag[i][1:] for i in range(len(pos_htag))]
#Count frequency of each word
pos_htag_freqcount = nltk.FreqDist(pos_htag)
pos_htag_df = pd.DataFrame({'Hashtag' : list(pos_htag_freqcount.keys()),
                            'Count' : list(pos_htag_freqcount.values())})


# In[20]:


#Select top 20 most frequent hashtags and plot them
most_frequent = pos_htag_df.nlargest(columns="Count", n = 20)
plt.figure(figsize=(16,5))
ax = sns.barplot(data=most_frequent, x= "Hashtag", y = "Count")
ax.set(ylabel = 'Count')
print 'First Show'
plt.show()


# Graph to show negative tweets

# In[21]:


#Repeat same steps for negative tweets
# print 'Cleaned Tweet :',train['cleaned_tweet']
negative_words = ' '.join([word for word in train['cleaned_tweet'][train['label'] == 1]])
neg_htag = [htag for htag in negative_words.split() if htag.startswith('#')]
neg_htag = [neg_htag[i][1:] for i in range(len(neg_htag))]
neg_htag_freqcount = nltk.FreqDist(neg_htag)
neg_htag_df = pd.DataFrame({'Hashtag' : list(neg_htag_freqcount.keys()),
                            'Count' : list(neg_htag_freqcount.values())})


# In[22]:


most_frequent = neg_htag_df.nlargest(columns="Count", n = 20)
plt.figure(figsize=(16,5))
ax = sns.barplot(data=most_frequent, x= "Hashtag", y = "Count")
plt.show()


# From both plots, we can conclude that hashtags are very important for sentiment analysis and should not be ignored.

# Words used like love, friend, happy are used in normal tweets whereas negative can be found in words like trump, black, politics etc.

# In[23]:


train.head(2)


# Rescale data using CountVectorizer
# ### CountVectorizer
# It’ll see the unique words in the complete para or content given to it and then does one hot encoding accordingly.
#

# ## Step 4: Split data into train and test dataset

# In[24]:


X_train, X_val, y_train, y_val = train_test_split(train['cleaned_tweet'], train['label'], random_state = 0)
X_train.shape, X_val.shape


# ## Step 5: Train the model

# In[29]:


cv = CountVectorizer()
vect = cv.fit(X_train)
X_train_vectorized = cv.transform(X_train)
X_train_vectorized


# ### Naive Bayes

# In[30]:


naive_base_model = MultinomialNB()
naive_base_model.fit(X_train_vectorized, y_train)
pred = naive_base_model.predict(vect.transform(X_val))
print('F1 :', f1_score(y_val, pred))


# ### Logistic Regression

# In[31]:


logistic_model_cv = LogisticRegression()
logistic_model_cv.fit(X_train_vectorized, y_train)
pred = logistic_model_cv.predict(vect.transform(X_val))
print('F1 :', f1_score(y_val, pred))


# Logistic Regression performed well then Naive Bayes for the default parameters. Thus, we will be using only Logistic Regression ahead.

# ### Tfidf
#  This one is similar to countvectorizer, however it removes the stopwords and stores the important words which might be used less but gives us more better features.And stores the frequency of the words.

# In[32]:


# Fit the TfidfVectorizer to the training data specifiying a minimum document frequency of 5
vect = TfidfVectorizer().fit(X_train)
print('Total Features =', len(vect.get_feature_names()))
X_train_vectorized = vect.transform(X_train)

logistic_model_tf = LogisticRegression()
logistic_model_tf.fit(X_train_vectorized, y_train)
pred = logistic_model_tf.predict(vect.transform(X_val))
print('Accuracy: ', f1_score(y_val, pred))


# tf-idf not performed well for this data.

# ## Step 7: Save the model in pickle file
#
# As logistic_model_cv gave us highest accuracy we'll go with it and save it to pickle file.
# We save our model to pickle file so that when we want to perform predictions on unseen data, we don't have to train our model again. Any object in python can be pickled so that it can be saved on disk. What pickle does is that it “serialises” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream.

# In[ ]:


# with open('model.pkl','wb') as file:
#     pickle.dump(logistic_model_cv, file)
#
#
# # In[ ]:
#
#
# ## Step 8: Test the model
# pre_processing = pickle.load(open('preprocessing.pkl', 'rb'))
# model = pickle.load(open('model.pkl', 'rb'))
