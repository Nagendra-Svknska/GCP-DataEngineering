from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'my_datasset_id'
table_id = 'stock_pricing'

table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

original_schema = table.schema
new_schema = original_schema[:]  # creates a copy of the schema
new_schema.append(bigquery.SchemaField("low_predicted", "float"))

table.schema = new_schema
table = client.update_table(table, ["schema"])  # API request

assert len(table.schema) == len(original_schema) + 1 == len(new_schema)