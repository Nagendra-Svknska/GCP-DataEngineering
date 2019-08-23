from apache_beam.options.pipeline_options import PipelineOptions,GoogleCloudOptions,StandardOptions,SetupOptions
import apache_beam as beam
# import pandas as pd
# import numpy as np
# import nltk
# import matplotlib.pyplot as plt
# import seaborn as sns

# import Utils as ut





def printer(data):
    print "enter the values"
    print data

def  clean_tweets(value):
    import re
    # print value['tweet']
    # print value.tweet
    value['cleaned_tweet'] = value.tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith('@')]))
    # print 'after @ removed',value

    value['cleaned_tweet'] = value.cleaned_tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith('#')]))
    # print 'after # removed', value

    value['cleaned_tweet'] = value.cleaned_tweet.apply(
        lambda x: ' '.join([word for word in x.split() if not word.startswith(' ')]))

    abc=str(value.cleaned_tweet)

    value['cleaned_tweet']=re.sub('[^A-Za-z0-9]+', ' ', abc)
    # print "value :", value

    return value


def makeDict_val(dataframe_val):

    # print dataframe_val
    label_val=''
    tweet_val=''
    cleaned_tweet_val=''
    sentiment=''
    list_val=[]
    # print dataframe_val
    # print 'exit'
    try :
        label_val=dataframe_val['label'].values
        tweet_val=dataframe_val['tweet'].values
        cleaned_tweet_val=dataframe_val['cleaned_tweet'].values
        sentiment=dataframe_val['sentiment'].values
    except Exception:
        print 'error'
    dict_val={}
    print "Label value :",type(label_val)
    print "Tweet value:",str(tweet_val)
    print "cleaned tweet value:",str(cleaned_tweet_val)
    print "sentiment :",str(sentiment)
    dict_val['tweet']=str(tweet_val)
    dict_val['cleaned_tweet']=cleaned_tweet_val
    dict_val['label']=label_val
    dict_val['sentiment']=sentiment
    list_val.append(dict_val)
    # print "dict_val :",dict_val

    return list_val



def  preprocessing1(value):
    from google.cloud import storage
    import unicodedata
    import pickle
    import pandas as pd

    val=unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    # print "Value :",val
    # print type(val)
    val_list=val.split(',')
    count=0
    id=''
    label=''
    tweet=''
    if (len(val_list) == 3):
        for i in val_list:

            if(count==0):
                # print "id :",i,type(i)
                try:
                    id =float(i)
                    # print 'No error'
                except ValueError:
                    print 'Error'
            elif(count==1):
                try :
                    # print "label :",i,type(i)
                    label=float(i)
                except Exception:
                    print 'error'
            elif(count==2):
                tweet=str(i)
            count=count+1

        dict_val = {'id': id, 'label': label, 'tweet': tweet}
        # print dict_val
        val = pd.DataFrame(dict_val,index=[0])
        val=clean_tweets(val)

        list_val_tweets = list(val['cleaned_tweet'])
        # print list_val_tweets

        storage_client = storage.Client()
        bucket = storage_client.get_bucket("test_dataflow_runne")

        blob = bucket.blob("tweet_sentiment_analysis.pkl")
        model_local = "TwitterSA_model.pkl"
        blob.download_to_filename(model_local)
        pickle_in = open("TwitterSA_model.pkl", "rb")
        reg = pickle.load(pickle_in)



        blob = bucket.blob("tweet_sentiment_analysis_countVect.pkl")
        model_local = "TwitterSA_Vect_model.pkl"
        blob.download_to_filename(model_local)
        pickle_in2 = open("TwitterSA_Vect_model.pkl", "rb")

        # pickle_in = open("tweet_sentiment_analysis.pickle", "rb")


        vect = pickle.load(pickle_in2)


        # print 'pickle files loaded'
        sen_val=reg.predict(vect.transform(list_val_tweets))
        # print sen_val
        # print reg.predict(vect.transform(list_val_tweets))
        if sen_val==0:
            val['sentiment']='positive'
        else :
            val['sentiment'] = 'negative'

    dict_val=makeDict_val(val)

    return dict_val



print 'enter the values'
options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'first-gcp-wordcount'

# !!! for Dataflow runner-start !!!

dataflow_options = ['--project=first-gcp-wordcount', '--job_name=test-job', '--temp_location=gs://test_dataflow_runne/temp']
dataflow_options.append('--staging_location=gs://test_dataflow_runne/stage')
options = PipelineOptions(dataflow_options)
gcloud_options = options.view_as(GoogleCloudOptions)
options.view_as(StandardOptions).runner = 'Dataflow'
# options.view_as(SetupOptions).save_main_session = True

# !!! for Dataflow runner-end !!!


table_schema = 'label:INTEGER, tweet:STRING, cleaned_tweet:STRING, sentiment:STRING'
table_spec = 'first-gcp-wordcount:my_datasset_id.Twitter_Sent_Analysis2'

p = beam.Pipeline(options=options)
lines=\
    (p|"ReadFromFile" >> beam.io.ReadFromText('gs://test_dataflow_runne/model', skip_header_lines=1)
      |"preprocessing the data 1 :" >> beam.ParDo(preprocessing1)
      # |" PRINTER :" >> beam.ParDo(printer)
      |"write to bigquery :" >> beam.io.WriteToBigQuery(table_spec,schema=table_schema,
       write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
       create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
     )
p.run()