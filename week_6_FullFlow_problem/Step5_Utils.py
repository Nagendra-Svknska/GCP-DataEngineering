def makeDataframe(data):
    import pandas as pd
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

        for value_in in value:
            key_in=str(value_in).split('.')[1].strip()

            if(key_in ==vol):
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
    dtfrm_val=pd.DataFrame(list_val,columns=('date','volume','close','high','open','low'))
    # print dtfrm_val.info()
    # print dtfrm_val.head()
    return dtfrm_val

def upload_to_bigquery(dataframe_val,table_ref,dataset_ref):

    print('entered upload to bigquery method')

    from google.cloud import bigquery
    import pandas

    client=bigquery.Client()
    dataset_ref = client.dataset(dataset_ref)
    table_ref = dataset_ref.table(table_ref)

    client.load_table_from_dataframe(dataframe_val, table_ref).result()



def Linear_regression_ML_Model(dataframe_val):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    # print dataframe_val
    x_val=dataframe_val.iloc[:,:-1].values
    y_val=dataframe_val.iloc[:,-1:].values

    x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.5)

    reg=LinearRegression()
    reg.fit(x_train,y_train)

    from sklearn import metrics
    y_predicted=reg.predict(x_val)

    dataframe_val=dataframe_val.assign(low_predicted=y_predicted)
    # print (metrics.accuracy_score(y_test,y_predicted))
    # print metrics.confusion_matrix(y_test,y_predicted)
    # print(reg.score(y_test,y_predicted))
    return dataframe_val

