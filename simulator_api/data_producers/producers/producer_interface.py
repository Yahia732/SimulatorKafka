from abc import ABC, abstractmethod


class ProducerInterface(ABC):
    @abstractmethod
    def produce(self, pandas_df):
        pass
