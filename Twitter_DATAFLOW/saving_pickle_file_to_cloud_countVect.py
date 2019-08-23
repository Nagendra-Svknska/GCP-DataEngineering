import pickle
import tensorflow as tf

pickle_in = open("tweet_sentiment_analysis_countVect.pickle", "rb")
reg = pickle.load(pickle_in)

filename = "gs://test_dataflow_runne/tweet_sentiment_analysis_countVect.pkl"
with tf.io.gfile.GFile(filename, 'wb') as f:
    pickle.dump(reg, f)