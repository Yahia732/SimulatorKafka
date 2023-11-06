from confluent_kafka import Consumer, KafkaError
import json

from simulator_api.configuration_manager.configuration_reader.configuration_reader_interface import ConfigurationReader


class KafkaReader(ConfigurationReader):
    def __init__(self, kafka_broker, topic, group_id):
        self.kafka_broker = kafka_broker
        self.topic = topic
        self.group_id = group_id
        self.consumer = None

    def configure_consumer(self):
        self.consumer = Consumer({
            'bootstrap.servers': self.kafka_broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([self.topic])

    def consume_messages(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)

                if msg is None:
                    continue

                if msg.error():

                    print("error in reading")
                else:
                    # Convert JSON message to Python dictionary
                    message_data = json.loads(msg.value())
                    return message_data

        except KeyboardInterrupt:
            pass

        finally:
            self.consumer.close()


