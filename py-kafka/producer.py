from kafka import KafkaProducer
from kafka.errors import KafkaError

import logging as log
producer = KafkaProducer(bootstrap_servers=['ubuntu1:9092','ubuntu2:9092','ubuntu3:9092'])
future = producer.send('test', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass
# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)