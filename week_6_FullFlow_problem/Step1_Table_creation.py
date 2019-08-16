from google.cloud import bigquery

def bq_create_table():
    print "entered the method"
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_datasset_id')

    # Prepares a reference to the table
    table_ref = dataset_ref.table('stock_pricing')

    try:
        bigquery_client.get_table(table_ref)
    except Exception:
        schema = [
            bigquery.SchemaField('volume', 'float'),
            bigquery.SchemaField('close', 'float'),
            bigquery.SchemaField('high', 'float'),
            bigquery.SchemaField('open', 'float'),
            bigquery.SchemaField('low', 'float'),
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = bigquery_client.create_table(table)
        print('table {} created.'.format(table.table_id))
        


print "entered the py file"
bq_create_table()
