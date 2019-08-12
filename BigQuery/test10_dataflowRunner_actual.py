import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
import pandas as pd
import numpy as np

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
    print type(val[['YearsExperience']])
    print type(val[['Salary']])
    reg = getPickle(val)
    x_val = np.array(val[['YearsExperience']])
    y_val_pred = reg.predict(x_val)
    y_val_actual=np.array(val[['Salary']])
    # list_val = []
    #
    # for i in range(len(x_val)):
    #         dicta = {}
    #
    #         try:
    #             # print type(x_val[i][0])
    #             xfloat_val=np.float(str(x_val[i][0]).strip())
    #             # print type(x)
    #             # dicta['YearsExperience'] = np.float(x_val[i][0])
    #             dicta['YearsExperience'] =xfloat_val
    #             # print type(y_val_actual)
    #             dicta['Actual Salary'] = np.float(y_val_actual[i][0])
    #             dicta['Predicted Salary'] =np.float( y_val_pred[i][0])
    #             list_val.append(dicta)
    #
    #         except Exception:
    #             dicta['Salary'] = 0
    #             dicta['YearsExperience'] = 0
    #             list_val.append(dicta)

    return y_val_pred

def getPickle(file_val):
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # print ("getPickle()", file_val)
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    # import numpy as np

    # file_val = pd.read_csv("/home/admin1/Desktop/sample datasets/Salary_Data.csv")
    x_val = np.array(file_val["YearsExperience"]).reshape(len(file_val["YearsExperience"]), 1)
    y_val = np.array(file_val["Salary"]).reshape(len(file_val["Salary"]), 1)
    # print(len(x_val))

    expval_train, expval_test, salval_train, salval_test = train_test_split(x_val, y_val, test_size=0.4)
    # print(expval_test)

    reg = LinearRegression()

    reg.fit(expval_train, salval_train)

    return reg

# Dataflow runner
options.view_as(StandardOptions).runner = 'dataflow'
options.view_as(SetupOptions).save_main_session = True
# options.view_as(StandardOptions).runner = 'Directrunner'

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
       | "Out_Put_File Cloud" >> beam.io.WriteToText('gs://test_dataflow_runne/predective.txt')
       # | "Out_Put_File Local" >> beam.io.WriteToText('output_val.txt')
 )






