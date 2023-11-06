from simulator_api.data_producers.producers.producer_interface import ProducerInterface
from pandas import DataFrame
import os


class CsvProducer(ProducerInterface):
    """
    A producer class for generating and saving data in a CSV file.


    Attributes:
    - identifier (str): The file path or identifier for the CSV file.
    """

    def __init__(self, identifier: str):
        """
        Initialize a CsvProducer instance.

        Parameters:
        - identifier (str): The file path or identifier for the CSV file.


        """
        self.identifier = identifier
        self._check_identifier_exits_or_create()

    def _check_identifier_exits_or_create(self):
        directory_path = os.path.dirname(self.identifier)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    def produce(self, data: DataFrame):
        """
        Produce and save data as a CSV file.

        Parameters:
        - data (pd.DataFrame): The data to be saved in the CSV file.

        Saves the provided data into a CSV file specified by the 'identifier'
        attribute.
        """

        data.to_csv(self.identifier)
