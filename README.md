# kafka-playground

# Setup

Install Virtual Env

```
pyenv virtualenv 3.6.7 kafka-playground
```

Install pykafka

```
pip install pykafka
```

Start Kafka Cluster on local machine, follow instructions here:

```
https://kafka.apache.org/quickstart
```

On a simpler note:

cd to the directory of kafka folder

```
cd ~/path/to/your/download/directory/kafka_2.12-2.3.0/
```

Make sure Zookeeper and Kafka is running by 

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

For convenience, you can open a terminal to show all the messages

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

# Command

Run the following python commands in two separate processes (terminals)

```
python manage.py start-consume-streaming-data
```

This will start to produce message into the Kafka

```
python manage.py start-consume-streaming-data
```

This will simply print out the message sent previously.
