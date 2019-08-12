
# to load pickle file from google cloud storage
from google.cloud import storage
storage_client = storage.Client()
bucket = storage_client.get_bucket("test_dataflow_runne")
blob = bucket.blob("salaries_pickle.pkl")
model_local = "test.pkl"
blob.download_to_filename(model_local)