from abc import ABC, abstractmethod

from simulator_api.data_producers.producers.producer_interface import ProducerInterface


class ProducerBuilderInterface(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> ProducerInterface:
        pass
