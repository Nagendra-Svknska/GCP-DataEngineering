import pickle
import tensorflow as tf

pickle_in = open("salaries.pickle", "rb")
reg = pickle.load(pickle_in)

filename = "gs://test_dataflow_runne/salaries_pickle.pkl"
with tf.io.gfile.GFile(filename, 'wb') as f:
    pickle.dump(reg, f)