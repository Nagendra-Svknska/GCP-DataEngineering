from google.cloud import bigquery

def exist_record():
    bigquery_client = bigquery.Client()

    query = ('SELECT id FROM `{}.{}.{}` WHERE id="{}" LIMIT 1'
            .format('first-gcp-wordcount', 'my_datasset_id', 'my_table_name', 'my_selected_id'))

    try:
        query_job = bigquery_client.query(query)
        is_exist = len(list(query_job.result())) >= 1
        print('Exist id: {}'.format('my_selected_id') if is_exist else 'Not exist id: {}'.format('my_selected_id'))
        return is_exist
    except Exception as e:
        print("Error")
        print(e)

    return False