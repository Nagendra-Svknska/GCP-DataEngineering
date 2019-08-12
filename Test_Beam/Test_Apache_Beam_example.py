import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions




p = beam.Pipeline('Directrunner')

lines = \
    (p | "reagfhfhfhgfdfromfile" >> beam.io.ReadFromText('gs://bucker_name/foklder_name/MBA.pkl-00000-of-00001')
     | "firsttreamfoirm" >> beam.FlatMap(lambda word: [len(word)])
     | "outpugdfgdtfile" >> beam.io.WriteToText('MBA2.mp4')
     )
p.run()


"""
readfrom train dataset file local storage for now only after that we have to read for google cloud storage
build ML model 
save pickle model in local now only after that we have to read for google cloud storage
prediction using test dataset and pickel file form local only after that we have to read for google cloud storage
save results local only after that we have to write to bigquery

"""
