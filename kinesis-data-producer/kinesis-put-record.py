import requests
import uuid
import json
import boto3
import time
import json
import random

client = boto3.client('kinesis', region_name='us-east-1')

while True:
    r = requests.get('https://randomuser.me/api/?exc=login')
    data = json.dumps(r.json()) 
    partition_key = str(uuid.uuid4())
    print(f'Data {partition_key}')
    client.put_record(
        StreamName='my-data-stream',
        Data=data,
        PartitionKey=partition_key
    )
    print('Data Length ', len(data))
    time.sleep(random.uniform(0,1))


