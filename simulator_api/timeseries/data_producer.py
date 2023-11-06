import pandas as pd
import os
from confluent_kafka import Producer


class DataProducer:
    """
    A base class for producing and saving time series data and associated metadata.

    Args:
        data (numpy.ndarray): The time series data.
        date_rng (pandas.DatetimeIndex): The date-time index for the time series data.
        anomaly (numpy.ndarray): An anomaly mask indicating the positions of anomalies in the data.
        file_name (str): The base file name for saving the data.
        dataset_number (int): The dataset number.

    Attributes:
        data (numpy.ndarray): The time series data.
        date_rng (pandas.DatetimeIndex): The date-time index for the time series data.
        anomaly (numpy.ndarray): An anomaly mask indicating the positions of outlier in the data.
        file_name (str): The base file name for saving the data.
        dataset_number (int): The dataset number.

    Methods:
        save(): Save the time series data and associated metadata.
    """

    def __init__(self, data, date_rng, anomaly, file_name, dataset_number):
        self.data = data
        self.date_rng = date_rng
        self.anomaly = anomaly
        self.file_name = file_name
        self.dataset_number = dataset_number

    def save(self):
        """
        Save the time series data and associated metadata.

        This method should be implemented by subclasses to specify the data-saving mechanism.

        Returns:
            None
        """
        pass


class DataProducerCSV(DataProducer):
    """
    A class for producing and saving time series data to a CSV file.

    Inherits from DataProducer.

    Methods:
        save(): Save the time series data to a CSV file with associated metadata.
    """

    def __init__(self, data, date_rng, anomaly, file_name, dataset_number):
        super().__init__(data, date_rng, anomaly, file_name, dataset_number)


    def save(self):
        """
        Save the time series data to a CSV file with associated metadata.

        Returns:
            None
        """
        # Check if 'sample_datasets/' directory exists, and create it if not
        if not os.path.exists('sample_datasets/'):
            os.makedirs('sample_datasets/')

        df = pd.DataFrame({'value': self.data, 'timestamp': self.date_rng, 'anomaly': self.anomaly})
        df.to_csv('sample_datasets/' + self.file_name + str(self.dataset_number) + '.csv', encoding='utf-8',
                  index=False)
class DataProducerkafka(DataProducer):
    def __init__(self, data, date_rng, anomaly, file_name, dataset_number):
        super().__init__(data, date_rng, anomaly, file_name, dataset_number)
        self.kafka_broker = "localhost:29092"
        self.topic = "TimeSeriesData"

        # Create a Kafka producer instance
        self.producer = Producer({"bootstrap.servers": self.kafka_broker})

    # Function to send a message to the Kafka topic

    def produce_message(self,message):
        self.producer.produce(self.topic, key=None, value=message)
    def save(self):
        """
        Save the time series data to kafka.

        Returns:
            None
        """
        # Check if 'sample_datasets/' directory exists, and create it if not
        # Send the simulated data to the Kafka topic
        simulated_data = pd.DataFrame({'value': self.data, 'timestamp': self.date_rng, 'anomaly': self.anomaly})
        simulated_data.to_json(orient='records')
        self.produce_message(simulated_data)
