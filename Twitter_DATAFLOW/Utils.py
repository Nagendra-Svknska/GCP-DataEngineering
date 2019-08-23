
def upload_to_bigquery(dataframe_val,table_ref,dataset_ref):

    print('entered upload to bigquery method')

    from google.cloud import bigquery
    import pandas

    client=bigquery.Client()
    dataset_ref = client.dataset(dataset_ref)
    table_ref = dataset_ref.table(table_ref)

    client.load_table_from_dataframe(dataframe_val, table_ref).result()

def testPrinter():
    print 'connected'
