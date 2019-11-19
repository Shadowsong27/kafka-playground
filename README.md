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

Start Kafka Cluster on local machine, follow instruction here:

```
https://kafka.apache.org/quickstart
```

Make sure Zookeeper and Kafka is running

# Command

Run the following command in two separate processes (terminals)

```
python manage.py start-consume-streaming-data
```

This will start to produce message into the Kafka

```
python manage.py start-consume-streaming-data
```

This will simply print out the message sent previously.