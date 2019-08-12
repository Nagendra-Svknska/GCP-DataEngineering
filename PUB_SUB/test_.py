import requests
from kafka import KafkaProducer
import json
import time
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=compact&apikey=0D8RR9NDGU7URNQT"

response = requests.get(url)
data=json.loads(response.text)




topicName ='test'

producer = KafkaProducer(bootstrap_servers=['10.0.0.8:9092','10.0.0.14:9092','10.0.0.7:9092','10.0.0.15:9092'],api_version=(0,10))
for i,j in data['Time Series (1min)'].items():
       producer.send('test',str(j))
       time.sleep(1)
producer.flush()