from configuration_manager.configuration_reader.configuration_reader_interface import ConfigurationReader
import pandas as pd

from configuration_manager.readers_serializers.csv_serialzier import CsvSerializer


class CSVReader(ConfigurationReader):
    """
    A configuration reader for reading configuration data from CSV files.

    """

    def __init__(self, identifier: str):
        """
        Initialize a CSVReader instance.

        Parameters:
        - identifier (str): The file path or identifier for the CSV file.

        Initializes the CSVReader by opening the CSV file and setting up a
        CsvSerializer instance for reading the data.
        """
        self.file = self.open(identifier)
        self.serializer = CsvSerializer(self.file)

    def open(self, identifier: str, **kwargs):
        """
        Opens and reads the CSV file specified by the 'identifier' and returns
        its contents as a pandas DataFrame

        Parameters:
        - identifier (str): The file path or identifier for the CSV file.
        - **kwargs: Additional keyword arguments for opening the CSV file.

        Returns:
        - pd.DataFrame: A pandas DataFrame containing the CSV data.

        """
        file = pd.read_csv(identifier)
        return file

    def get(self, config_var_name: str):
        """
        Get a specific configuration variable from the CSV data.

        Parameters:
        - config_var_name (str): The name of the configuration variable.

        Returns:
        - Any :  The value of the specified configuration variable.

        """
        return self.serializer.__dict__()[config_var_name]
