import argparse
import logging
import re
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
import tensorflow as tf
import pickle
from apache_beam.io.gcp.internal.clients import bigquery

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'serene-vehicle-247610'
google_cloud_options.job_name = 'testingjob'
google_cloud_options.staging_location = 'gs://akanksha_bucket_1/staging'
google_cloud_options.temp_location = 'gs://akanksha_bucket_1/temp'
#options.view_as(StandardOptions).runner = 'DataFlowRunner'
options.view_as(StandardOptions).runner = 'DirectRunner'

table_spec = bigquery.TableReference(
projectId='serene-vehicle-247610',
datasetId='my_new_dataset',
tableId='salary_2')



table_schema = {'fields': [
{'name': 'Years', 'type': 'STRING', 'mode': 'REQUIRED'},
{'name': 'Salary', 'type': 'STRING', 'mode': 'REQUIRED'}
]}

def MLmodel(data):
    #print(data)
    dataset = pd.read_csv('Salary_Data.csv')
    #print(dataset)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #filename = "gs://akanksha_bucket_1/salary_data2.pkl"
    #with tf.io.gfile.GFile(filename, 'wb') as f
    #pickle.dump(regressor, f)
    #pred = regressor.predict(X_test)

    storage_client = storage.Client()
    bucket = storage_client.get_bucket("akanksha_bucket_1")
    blob = bucket.blob("salary_data2.pkl")
    model_local = "salary_data2.pkl"
    blob.download_to_filename(model_local)

    # pkk = pickle.load(open(model_local, 'rb'))
    # print (
    #  pkk = pickle.load(open(model_local, 'rb'))
    # print (type(pkk))
    # pred = pkk.predict(X_test)
    # print(pred)
    return pred



p = beam.Pipeline(options=options)

lines=\
(p | "ReadFromFile" >> beam.io.ReadFromText('gs://akanksha_bucket_1/Salary_Data.csv')


|'Map record to key' >> beam.Map(lambda record: ('Data', record))
| 'GroupBy data' >> beam.GroupByKey()
# | "print data" >> beam.ParDo(printdata)
| 'Build Model' >> beam.ParDo(MLmodel)
# | 'Combine' >> beam.CombineValues(beam.combiners.Dict)
# 'Write output to file' >> beam.io.WriteToText('gs://akanksha_bucket_1/SalaryOou.csv')
|beam.io.WriteToBigQuery(
table_spec, schema=table_schema,
write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
)

p.run()