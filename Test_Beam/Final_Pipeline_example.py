import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

import apache_beam as beam
import pickle
from apache_beam.options.pipeline_options import PipelineOptions

def getmodel(file_val):

    x_val=np.array(file_val[['YearsExperience']])
    # print(x_val,'',type(x_val),'',np.shape(x_val))
    pickle_in = open("salaries.pickle", "rb")
    reg=pickle.load(pickle_in)
    # print (type(reg))
    y_val=reg.predict(x_val)

    return y_val


def printer(data_item):
    print (data_item)
    # print ('val')


def makeDataframe(data):
    val=data[1]
    val = pd.DataFrame(val,columns=('YearsExperience','Salary'))
    val=val.iloc[1:,:]
    reg_val=getmodel(val)
    return reg_val


p = beam.Pipeline('Directrunner')
model_val=getmodel
lines = \
    (p | "ReadFromFile" >> beam.io.ReadFromText('/home/admin1/Desktop/sample datasets/Salary_Data.csv')
     # | "firsttreamfoirm" >> beam.Map(getmodel)
     | "splitter using beam.map" >> beam.Map(lambda rec:(rec.split(',')))
     # | "Print the data" >> beam.ParDo(printer)
     | 'Map record to 1' >> beam.Map(lambda record: ('aa',record))
     | 'Group by data'   >> beam.GroupByKey()
     |  "Print the data 2" >> beam.ParDo(printer)
     | "Build the model"  >> beam.ParDo(makeDataframe)
     # | "Print the data" >> beam.ParDo(printer)
     | "outpugdfgdtfile" >> beam.io.WriteToText('Output_PipeLine.txt')
     )
p.run()


