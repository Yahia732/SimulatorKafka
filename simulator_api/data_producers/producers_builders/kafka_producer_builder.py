from simulator_api.data_producers.producers.kafka_producer import KafkaProducer
from simulator_api.data_producers.producers_builders.producer_builder_interface import ProducerBuilderInterface


class KafkaProducerBuilder(ProducerBuilderInterface):
    """
    A builder class to be used by a factory class for creating KafkaProducer instances to.

    """

    def __call__(self,broker) -> KafkaProducer:


        self._instance = KafkaProducer(broker)
        return self._instance