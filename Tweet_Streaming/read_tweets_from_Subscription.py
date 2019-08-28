import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions,GoogleCloudOptions,StandardOptions



def printer(data_item):
    print(data_item)




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
            (subscription="projects/first-gcp-wordcount/subscriptions/subscribe_test_twitter").with_output_types(bytes)
      # | "map the message :" >> beam.Map(lambda x:p)
      | "print the value :" >> beam.ParDo(printer)
      # | "makedataframe :" >> beam.ParDo(dataframe_val)
      # | "print the value 2:">> beam.ParDo(printer)
     )
p.run().wait_until_finish()