import pandas as pd
import apache_beam as beam



def sync_pull(project_id, subscription_name):

    from google.cloud import pubsub_v1

    subscriber=pubsub_v1.SubscriberClient()
    subscription_path=subscriber.subscription_path(project_id, subscription_name)
    NUM_MESSAGES = 1

    # The subscriber pulls a specific number of messages.
    response = subscriber.pull(subscription_path, max_messages=NUM_MESSAGES)

    ack_ids = []
    for received_message in response.received_messages:
     # print("Received: {}".format(received_message.message.data))
     pass
    ack_ids.append(received_message.ack_id)

    # Acknowledges the received messages so they will not be sent again.
    subscriber.acknowledge(subscription_path, ack_ids)

    print("Received and acknowledged {} messages. Done.".format(NUM_MESSAGES))
    # [END pubsub_subscriber_sync_pull]
    return received_message.message.data



def makeDataframe(val):
    list_val = []
    for i in val:
        # print i
        key = i
        value = val[i]
        vol_val = ''
        cls_val = ''
        high_val = ''
        opn_val = ''
        low_val = ''
        vol = str("volume")
        cls = str("close")
        hgh = str("high")
        opn = str("open")
        lw = str("low")

        # print value
        # print type(value)
        #
        for value_in in value:
            # print value_in
            # print type(value_in)

            key_in = str(value_in).split('.')[1].strip()
            # key_in=str(key_in).upper()
            # print type(key_in)
            # # print value[value_in]
            # print vol

            # print 'Key_in :',key_in,", volume:",vol
            # print type(key_in), len(key_in), len(vol)
            # print key_in == vol
            # if(key_in == vol):
            #     print 'true'

            if (key_in == vol):
                # print 'reached'
                vol_val = value[value_in]
            elif (key_in == cls):
                cls_val = value[value_in]
            elif (key_in == hgh):
                high_val = value[value_in]
            elif (key_in == opn):
                opn_val = value[value_in]
            elif (key_in == lw):
                low_val = value[value_in]
        list_val.append([key, vol_val, cls_val, high_val, opn_val, low_val])
        # print (
        #     'vol_val :', vol_val, ',cls_val :', cls_val, ',high_val :', high_val, ',opn_val :', opn_val, ',low_val :',
        #     low_val)
        # print [key,vol_val,cls_val,high_val,opn_val,low_val]

        # dtfrm_val=dtfrm_val.append([key,vol_val,cls_val,high_val,opn_val,low_val], ignore_index=True)
    # print list_val
    # val = pd.DataFrame(val,columns=('YearsExperience','Salary'))

    dtfrm_val = pd.DataFrame(list_val, columns=('date', 'volume', 'close', 'high', 'open', 'low'))
    return dtfrm_val


# val=sync_pull('first-gcp-wordcount','terminator2sub')
# # print ('type :',type(val))
# # print ('val :',val)
# val=eval(val)
# # print ('type 2 :',type(val))
# val=val['Time Series (1min)']
# val=makeDataframe(val)
# print val






