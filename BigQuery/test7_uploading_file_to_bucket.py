from google.cloud import bigquery
from google.cloud import storage

def gcs_upload_blob():
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('test_dataflow_runne')
    # blob = bucket.blob('gs://path/to/file.name')
    # blob = bucket.blob('gs://test_big_query')
    blob = bucket.blob('model')


    blob.upload_from_filename('/home/admin1/Desktop/sample datasets/Salary_Data.csv')

    print('File {} uploaded to {}.'.format(
        '/path/to/source.csv',
        'gs://path/to/upload.csv'))

gcs_upload_blob()

print "abc"
gcs_upload_blob()




