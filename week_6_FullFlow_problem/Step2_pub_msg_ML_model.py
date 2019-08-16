import requests
import json


def GetData():
    url ="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=compact&apikey=0D8RR9NDGU7URNQT"

    response = requests.get(url)
    data=json.loads(response.text)
    data=str(data)
    return data

def publish_messages(project_id, topic_name,message):
    """Publishes multiple messages to a Pub/Sub topic."""
    # [START pubsub_quickstart_publisher]
    # [START pubsub_publish]
    from google.cloud import pubsub_v1

    # TODO project_id = "Your Google Cloud Project ID"
    # TODO topic_name = "Your Pub/Sub topic name"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = publisher.topic_path(project_id, topic_name)

    data=message
    data=data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())


    print('Published messages.')
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]

project_id='first-gcp-wordcount'
topic_name='terminator2'
message=GetData()
publish_messages(project_id, topic_name,message)