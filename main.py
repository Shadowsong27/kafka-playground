from pykafka import KafkaClient
import random
# assume default port
client = KafkaClient(hosts="127.0.0.1:9092")

# assume following quick start docs on Kafka docs
topic = client.topics['test']


def publish_data():
    while True:
        with topic.get_sync_producer() as producer:
            for i in range(4):
                producer.produce(f'test message {random.randint(0, 10000)}'.encode("utf-8"))


def consume_data():
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print(f"This is the #{message.offset} message I have consumed, message: {message.value.decode('utf-8')}")
