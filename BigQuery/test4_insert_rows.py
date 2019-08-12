from google.cloud import bigquery

def export_items_to_bigquery():
    print "entered the method"
    # Instantiates a client
    bigquery_client = bigquery.Client()

    # Prepares a reference to the dataset
    dataset_ref = bigquery_client.dataset('my_datasset_id')

    table_ref = dataset_ref.table('my_table_name')
    table = bigquery_client.get_table(table_ref)  # API call

    rows_to_insert = [
        (u'Phred Phlyntstone', 32),
        (u'Wylma Phlyntstone', 29),
    ]
    errors = bigquery_client.insert_rows(table, rows_to_insert)  # API request
    assert errors == []

print "entered the py file "
export_items_to_bigquery()