from google.cloud import bigquery

# TODO(developer): Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the model to fetch.
table_id = 'first-gcp-wordcount.my_datasset_id.my_table_name'

table = client.get_table(table_id)
# print client.get_table(table_id)

print(
    "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
)

# View table properties
print("Table schema: {}".format(table.schema))
print("Table description: {}".format(table.description))
print("Table has {} rows".format(table.num_rows))