from google.cloud import bigquery

def bq_create_table():
    print "entered the method"
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('my_datasset_id')

    # Prepares a reference to the table
    table_ref = dataset_ref.table('my_table_name')

    try:
        bigquery_client.get_table(table_ref)
    except Exception:
        schema = [
            bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED'),
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = bigquery_client.create_table(table)
        print('table {} created.'.format(table.table_id))
        


print "entered the py file"
bq_create_table()
