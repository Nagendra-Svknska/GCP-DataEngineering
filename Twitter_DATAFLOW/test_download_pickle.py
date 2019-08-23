from google.cloud import storage
import pickle

storage_client = storage.Client()
bucket = storage_client.get_bucket("test_dataflow_runne")

blob = bucket.blob("tweet_sentiment_analysis.pkl")
model_local = "TwitterSA_model.pkl"
blob.download_to_filename(model_local)
pickle_in = open("TwitterSA_model.pkl", "rb")
reg = pickle.load(pickle_in)
# vect = pickle.load(pickle_in)


blob = bucket.blob("tweet_sentiment_analysis_countVect.pkl")
model_local = "TwitterSA_Vect_model.pkl"
blob.download_to_filename(model_local)
pickle_in2 = open("TwitterSA_Vect_model.pkl", "rb")

# pickle_in = open("tweet_sentiment_analysis.pickle", "rb")


vect = pickle.load(pickle_in2)
#
#
#
# from google.cloud import storage
# storage_client = storage.Client()
# bucket = storage_client.get_bucket("test_dataflow_runne")
# blob = bucket.blob("salaries_pickle.pkl")
# model_local = "test.pkl"
# blob.download_to_filename(model_local)