import pandas as pd
from confluent_kafka import Producer
from simulator_api.data_producers.producers.producer_interface import ProducerInterface



class KafkaProducer(ProducerInterface):
    """
        Initialize a KafkaProducer instance.




        """

    def __init__(self,simulator,broker,topic):
        self.timestamp = simulator.timestamp
        self.attributeId = simulator.attributeId
        self.value = simulator.value
        self.assetId = simulator.assetId
        self._check_identifier_exits_or_create()
        self.kafka_broker = broker
        self.topic = topic
        self.producer = Producer({"bootstrap.servers": self.kafka_broker})

    def produce_message(self, message):
        self.producer.produce(self.topic, key=None, value=message)

    def kafka_producer(self):
        """
        Save the time series data to kafka.

        Returns:
            None
        """
        # Send the simulated data to the Kafka topic
        simulated_data = pd.DataFrame({'attributeId': self.attributeId, 'timestamp': self.timestamp, 'assetId': self.assetId,'value':self.value})
        for index, row in simulated_data.iterrows():

            serliazed_message=row.to_json(orient='records')
            self.produce_message(serliazed_message)
