import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

import apache_beam as beam
import pickle
from apache_beam.options.pipeline_options import PipelineOptions

def getmodel(file_val):
    print "Entered the value"
    x_val=np.array(file_val[['name']])

    # print(x_val,'',type(x_val),'',np.shape(x_val))
    pickle_in = open("salaries.pickle", "rb")
    reg=pickle.load(pickle_in)
    # print (type(reg))
    y_val=reg.predict(x_val)
    list_val=[]
    # print ("X value :",x_val)
    # print ("Y value :",y_val)
    # print (len(x_val))
    for i in range(len(x_val)):
            dicta = {}
            # print ('x_val :',type(x_val[i][0]),'y_val :',y_val[i][0])
            # tup=(x_val[i][0],y_val[i][0])

            try:
                dicta['name'] = np.float(x_val[i][0])
                dicta['age']=y_val[i][0]
                list_val.append(dicta)

            except Exception:
                dicta['name'] = 0
                dicta['age'] = 0
                list_val.append(dicta)
            # print (type(y_val[i][0]))
            # x=np.float(x_val[i][0])
            # print (type(x))
            # dicta[x_val[i][0]]=y_val[i][0]

    print list_val
    # for x in np.nditer(x_val):
    #     print x
    # for x in range(x_val):
    #    print ("X value :",type(x_val))
    #    print ("Y value :",type(y_val))




    return list_val

def printer(data_item):
    print data_item

def makeDataframe(data):
    val=data[1]
    val = pd.DataFrame(val,columns=('name','age'))
    val=val.iloc[1:,:]

    reg_val=getmodel(val)
    return reg_val

p = beam.Pipeline('Directrunner')

# model_val=getmodel
table_schema = 'name:FLOAT, age:FLOAT'
table_spec = 'first-gcp-wordcount:my_datasset_id.my_table_name3'
lines = \
    (p | "ReadFromFile" >> beam.io.ReadFromText('gs://test_big_query/gs://test_big_query')
     # | "firsttreamfoirm" >> beam.Map(getmodel)
     | "splitter using beam.map" >> beam.Map(lambda rec:(rec.split(',')))
     # | "Print the data" >> beam.ParDo(printer)
     | 'Map record to 1' >> beam.Map(lambda record: ('aa',record))
     | 'Group by data'   >> beam.GroupByKey()
     # |  "Print the data 2" >> beam.ParDo(printer)
     | "Build the model"  >> beam.ParDo(makeDataframe)
     # | "Print the data 3" >> beam.ParDo(printer)
     | "outpugdfgdtfile" >> beam.io.WriteToText('Output_PipeLine.txt')
     # | beam.io.WriteToBigQuery(
     #   table_spec,
     #   schema=table_schema,
     #   # write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
     #   create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
    )
p.run()


