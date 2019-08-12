import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
import pandas as pd
import pickle
import numpy as np
import tensorflow


#  #moving a file into a bucket
# def gcs_upload_blob():
#     """Uploads a file to the bucket."""
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket('test_dataflow_runne')
#     # blob = bucket.blob('gs://path/to/file.name')
#     blob = bucket.blob('gs://test_dataflow_runne')
#
#
#     blob.upload_from_filename('/home/admin1/Desktop/sample datasets/Salary_Data.csv')
#
#     print('File {} uploaded to {}.'.format(
#         '/path/to/source.csv',
#         'gs://path/to/upload.csv'))
#
# gcs_upload_blob()
#
# print "abc"
# gcs_upload_blob()

# # moving pickle file to bucket
# from google.cloud import bigquery
# from google.cloud import storage
#
# def gcs_upload_blob():
#     """Uploads a file to the bucket."""
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket('test_dataflow_runne')
#     # blob = bucket.blob('gs://path/to/file.name')
#     blob = bucket.blob('gs://salaries_pickle')
#
#
#     blob.upload_from_filename('salaries.pickle')
#
#     print('File {} uploaded to {}.'.format(
#         '/path/to/source.csv',
#         'gs://path/to/upload.csv'))
#
# gcs_upload_blob()
#
# print "abc"
# gcs_upload_blob()





PROJECT='first-gcp-wordcount'
BUCKET='test_dataflow_runne'

input_filename = 'gs://test_dataflow_runne/gs://test_dataflow_runne'
output_filename = 'gs://test_dataflow_runne/gs://test_dataflow_runne/output.txt'

dataflow_options = ['--project=first-gcp-wordcount', '--job_name=test-job', '--temp_location=gs://test_dataflow_runne/temp']
dataflow_options.append('--staging_location=gs://test_dataflow_runne/stage')
options = PipelineOptions(dataflow_options)
gcloud_options = options.view_as(GoogleCloudOptions)


def printer (dataval):
    print dataval

class Split(beam.DoFn):
    def process(self, element):
        """
        Splits each row on commas and returns a dictionary representing the
        row
        """
        printer(element)
        YearsExperience, Salary = element.split(",")
        printer(YearsExperience)
        printer(Salary)
        return [{
            'country': float(YearsExperience),
            'duration': float(Salary),
        }]

def getFinalList(data_val):
    print 'entered the method'
    # print (data_val[1])
    val=data_val[1]
    val = pd.DataFrame(val, columns=('YearsExperience', 'Salary'))
    val=val.iloc[1:,:]
    # print (val)
    reg = getPickle()
    x_val = np.array(val[['YearsExperience']])
    y_val_pred = reg.predict(x_val)
    y_val_actual=np.array(val[['Salary']])
    list_val = []

    for i in range(len(x_val)):
            dicta = {}

            try:
                dicta['YearsExperience'] = np.float(x_val[i][0])
                dicta['Actual Salary'] = y_val_actual[i][0]
                dicta['Predicted Salary'] = y_val_pred[i][0]
                list_val.append(dicta)

            except Exception:
                dicta['Salary'] = 0
                dicta['YearsExperience'] = 0
                list_val.append(dicta)

    return list_val

def getPickle():
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("test_dataflow_runne")
    blob = bucket.blob("salaries_pickle.pkl")
    # print ('model local ')
    model_local = "salaries_pickle.pkl"
    # print type(blob)
    blob.download_to_filename(model_local)
    reg=pickle.load(open('salaries_pickle.pkl','rb'))
    # print reg
    return  reg

# Dataflow runner
# options.view_as(StandardOptions).runner = 'dataflow'
options.view_as(SetupOptions).save_main_session = True

options.view_as(StandardOptions).runner = 'Directrunner'

# with beam.pipeline()
with beam.Pipeline(options=options) as p:
 rows=(p
       |'read from file '>> beam.io.ReadFromText(input_filename)
       # |'Value Test' >> beam.ParDo(printer)
       | 'Take the column value off' >> beam.Map(lambda rec:(rec.split(',')))
       | 'Map record to 1' >> beam.Map(lambda record: ('aa', record))
       | 'Group by data' >> beam.GroupByKey()
       # | 'print the values1' >> beam.ParDo(printer)
       | 'Group by data2' >> beam.ParDo(getFinalList)
       # | 'Split the values' >> beam.ParDo(Split())
       # | 'print the values3' >> beam.ParDo(printer)
       # | "Out_Put_File Cloud" >> beam.io.WriteToText('gs://test_dataflow_runne/predective.txt')
       | "Out_Put_File Local" >> beam.io.WriteToText('output_val.txt')
 )






