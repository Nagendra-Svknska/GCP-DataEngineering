from google.cloud import bigquery

def bq_create_dataset():
    print ('entered the method')
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_datasset_id')

    try:

        bigquery_client.get_dataset(dataset_ref)
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset = bigquery_client.create_dataset(dataset)
        print('Dataset {} created.'.format(dataset.dataset_id))


print ('enter the data')
bq_create_dataset()