
import requests
import json
import pandas as pd

def GetData():
    url ="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=compact&apikey=0D8RR9NDGU7URNQT"

    response = requests.get(url)
    data=json.loads(response.text)
    # print(data)
    return data

data=GetData()

# print data['Time Series (1min)']
val=data['Time Series (1min)']
# print type(val)

list_val=[]
for i in val:
    # print i
    key=i
    value = val[i]
    vol_val=''
    cls_val=''
    high_val=''
    opn_val=''
    low_val=''
    vol = str("volume")
    cls=str("close")
    hgh=str("high")
    opn=str("open")
    lw=str("low")




    # print value
    # print type(value)
    #
    for value_in in value:
        # print value_in
        # print type(value_in)

        key_in=str(value_in).split('.')[1].strip()
        # key_in=str(key_in).upper()
        # print type(key_in)
        # # print value[value_in]
        # print vol

        # print 'Key_in :',key_in,", volume:",vol
        # print type(key_in), len(key_in), len(vol)
        # print key_in == vol
        # if(key_in == vol):
        #     print 'true'

        if(key_in ==vol):
            # print 'reached'
            vol_val = float(value[value_in])
        elif(key_in==cls):
            cls_val =float(value[value_in])
        elif (key_in == hgh):
            high_val = float(value[value_in])
        elif (key_in ==opn):
            opn_val = float(value[value_in])
        elif (key_in ==lw):
            low_val = float(value[value_in])
    list_val.append([key, vol_val, cls_val, high_val, opn_val, low_val])
    # print (
    #     'vol_val :', vol_val, ',cls_val :', cls_val, ',high_val :', high_val, ',opn_val :', opn_val, ',low_val :',
    #     low_val)
    # print [key,vol_val,cls_val,high_val,opn_val,low_val]

    # dtfrm_val=dtfrm_val.append([key,vol_val,cls_val,high_val,opn_val,low_val], ignore_index=True)
# print list_val
# val = pd.DataFrame(val,columns=('YearsExperience','Salary'))

dtfrm_val=pd.DataFrame(list_val,columns=('date','volume','close','high','open','low'))
# print dtfrm_val.info()
# print dtfrm_val.head()

dtfrm_val=dtfrm_val.iloc[:,1:]
# print dtfrm_val

import Utils as ut

ut.Linear_regression_ML_Model(dtfrm_val)
