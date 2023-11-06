from simulator_api.data_producers.producers.csv_file_producer import CsvProducer
from simulator_api.data_producers.producers_builders.producer_builder_interface import ProducerBuilderInterface


class CsvProducerBuilder(ProducerBuilderInterface):
    """
    A builder class to be used by a factory class for creating CsvProducer instances to.

    """

    def __call__(self, location: str) -> CsvProducer:
        """
        Create or retrieve a CsvProducer instance.

        Parameters:
        - location (str): The location where the CsvProducer will generate CSV files.

        Returns:
        - CsvProducer: A CsvProducer instance configured with the specified location.

        """
        self._instance = CsvProducer(location)
        return self._instance
