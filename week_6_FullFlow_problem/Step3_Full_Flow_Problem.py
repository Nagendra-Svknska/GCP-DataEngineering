import apache_beam as beam
import recieve_msg_sync_pull as rcv_msg
from apache_beam.options.pipeline_options import PipelineOptions,GoogleCloudOptions,StandardOptions
import Utils as ut


def make_df_value(data):
    val = eval(data)
    # # print ('type 2 :',type(val))
    val=val['Time Series (1min)']
    val=rcv_msg.makeDataframe(val)
    # print val
    return val

def dataframe_val(data_item):
    print ("entered the dataframe")
    dat_val = str(data_item)
    # print ('String value :',dat_val)
    dat_val_dict = eval(dat_val)
    # print ('Dict value :', dat_val_dict)

    value_val = ut.makeDataframe(dat_val_dict)
    # print ("Value_val : ", value_val)
    value_val = value_val.iloc[:, 1:]

    pred_val=ut.Linear_regression_ML_Model(value_val)

    ut.upload_to_bigquery(pred_val,'stock_pricing','my_datasset_id')
    return value_val

def printer(data_item):
    print('entered')




options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'first-gcp-wordcount'

# google_cloud_options.job_name = 'myjob'
# google_cloud_options.staging_location = 'gs://your-bucket-name-here/staging'
# google_cloud_options.temp_location = 'gs://your-bucket-name-here/temp'
options.view_as(StandardOptions).runner = 'Directrunner'
options.view_as(StandardOptions).streaming = True

p = beam.Pipeline(options=options)

lines=\
    (p| "read data from subscription :" >> beam.io.ReadFromPubSub
            (subscription="projects/first-gcp-wordcount/subscriptions/terminator2sub").with_output_types(bytes)
      # | "map the message :" >> beam.Map(lambda x:p)
      # | "print the value :" >> beam.ParDo(printer)
      | "makedataframe :" >> beam.ParDo(dataframe_val)
      # | "print the value 2:">> beam.ParDo(printer)
     )
p.run().wait_until_finish()