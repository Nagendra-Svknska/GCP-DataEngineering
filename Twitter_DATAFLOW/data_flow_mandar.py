import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions,SetupOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions




dataflow_options = ['--project=lofty-shine-248403', '--job_name=newjob', '--temp_location=gs://testing-gcp-mandar/temp']
dataflow_options.append('--staging_location=gs://testing-gcp-mandar/staging')
options = PipelineOptions(dataflow_options)
gcloud_options = options.view_as(GoogleCloudOptions)

# Dataflow runner
options.view_as(StandardOptions).runner = 'Dataflow'
# options.view_as(SetupOptions).save_main_session = True
# options.view_as(StandardOptions).streaming = True

table_schema = {'fields': [
{'name': 'Tweet', 'type': 'STRING'},
{'name': 'Sentiment', 'type': 'STRING'}
]}



def preprocess(data):
    import re
    l = []
    ndata=data.split(',')
    tweet = " ".join(ndata[1:])

    tweet = ' '.join([word for word in tweet.split() if not word.startswith('@')])
    tweet = ' '.join([word for word in tweet.split() if not word.startswith('#')])
    tweet = ' '.join([word for word in tweet.split() if not word.startswith(' ')])
    tweet = re.sub('[^A-Za-z0-9]+', ' ', tweet)
    l.append(tweet)
    return l

def prediction(tweet):
    import pickle
    from google.cloud import storage

    storage_client = storage.Client()
    bucket = storage_client.get_bucket("testing-gcp-mandar")

    blob = bucket.blob("model.pkl")
    model_local = "TwitterSA_model.pkl"
    blob.download_to_filename(model_local)
    pickle_in = open("TwitterSA_model.pkl", "rb")
    model = pickle.load(pickle_in)

    blob=bucket.blob("prep.pkl")
    model_local = "TwitterSA_prep.pkl"
    blob.download_to_filename(model_local)
    pickle_prep = open("TwitterSA_prep.pkl", "rb")
    prep = pickle.load(pickle_prep)


    # print tweet
    ntweet=[tweet]
    x=prep.transform(ntweet)
    pred=model.predict(x)
    l1 = []
    temp = {}
    temp['Tweet'] = str(tweet)
    if(str(pred).replace('[', '').replace(']', '') == '0'):
        temp['Sentiment'] = 'Positive'
    else:
            temp['Sentiment'] = 'Negative'
    l1.append(temp)
    print(l1)
    return l1

p = beam.Pipeline(options=options)

lines = \
(p | 'Read Data From PubSub' >> beam.io.ReadFromText('test_tweets_anuFYb8.csv', skip_header_lines=1)
| 'preprocess' >> beam.ParDo(preprocess)
| 'machine learning' >> beam.ParDo(prediction)
| 'storing in bigQ' >> beam.io.WriteToBigQuery(
schema=table_schema,
table="lofty-shine-248403:my_new_datasset.TweetHisSentimentLabeled")

)

p.run()