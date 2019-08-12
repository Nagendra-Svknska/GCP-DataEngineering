from google.cloud import bigquery
# export GOOGLE_APPLICATION_CREDENTIALS="/home/admin1/GOOGLE CLOUD Authentication/first-gcp-wordcount-7d90b495702d.json"



client = bigquery.Client()
# bigquery.client.fr

query_job = client.query("""
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10""")

results = query_job.result()

for row in results:
    print("{} : {} views".format(row.url, row.view_count))


        # import os
        #
        # print('Credendtials from environ: {}'.format(
        #     os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
