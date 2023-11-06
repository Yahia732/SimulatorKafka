import yaml

from configuration_manager.configuration_reader.configuration_reader_interface import ConfigurationReader
from configuration_manager.readers_serializers.yaml_serializer import YamlSerializer


class YamlReader(ConfigurationReader):
    """
    A configuration reader for reading configuration data from YAML files.

    """

    def __init__(self, identifier: str):
        """
        Initialize a YamlReader instance.

        Parameters:
        - identifier: The file path or identifier for the YAML file.

        """
        self.file = self.open(identifier)
        self.serializer = YamlSerializer(self.file)

    def open(self, identifier: str, **kwargs):
        """
        Open and read a YAML file.

        Parameters:
        - identifier: The file path or identifier for the YAML file.
        - **kwargs: Additional keyword arguments for opening the YAML file.

        Returns:
        - dict: A dictionary containing the YAML data.

        """
        with open(identifier, 'r') as f:
            yml_data = yaml.safe_load(f)
        return yml_data

    def get(self, config_var_name: str):
        """
        Get a specific configuration variable from the YAML data.

        Parameters:
        - config_var_name: The name of the configuration variable.

        Returns:
        - Any: The value of the specified configuration variable from the YAML data.

        """
        return self.serializer.__dict__()[config_var_name]
