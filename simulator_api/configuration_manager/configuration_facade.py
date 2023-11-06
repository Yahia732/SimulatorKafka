from simulator_api.enums.data_type_enum import DataTypeEnum


class ConfigurationFacade:
    """
    A facade class for accessing configuration data through a reader.
    """

    def __init__(self, reader):
        """
        Initialize a ConfigurationFacade instance.

        Parameters:
        - reader: An instance of a configuration reader.

        """
        self.reader = reader

    @property
    def cyclic_period(self):
        """
        Get the cyclic period ( in years)  from the configuration ,

        Returns:
        - float : The cyclic period specified in the configuration.
        """
        return float(self.reader.get("cyclic_period"))

    @property
    def cyclic_amplitude(self):
        """
        Get the cyclic amplitude from the configuration.

        Returns:
        - float : The cyclic amplitude specified in the configuration.
        """
        return float(self.reader.get("cyclic_amplitude"))

    @property
    def noise_level(self):
        """
        Get the noise level from the configuration.

        Returns:
        - float: The noise level specified in the configuration.
        """
        return float(self.reader.get("noise_level"))

    @property
    def start_date(self):
        """
        Get the start date from the configuration.

        Returns:
        - string: The start date specified in the configuration.
        """
        return self.reader.get("start_date")

    @property
    def end_date(self):
        """
        Get the end date from the configuration.

        Returns:
        - string: The end date specified in the configuration.
        """
        return self.reader.get("end_date")

    @property
    def seasonality(self):
        """
        Get the seasonality from the configuration.

        Returns:
        - list[dict]: The seasonality componenets specified in the configuration.
        """
        return self.reader.get("seasonality")

    @property
    def frequency(self):
        """
        Get the frequency from the configuration.

        Returns:
        - string: The frequency specified in the configuration.
        """
        return self.reader.get("frequency")

    @property
    def trend_coefficients(self):
        """
        Get the trend coefficients from the configuration.

        Returns:
        - List[float]: A list of trend coefficients specified in the configuration.
        """
        return [float(a) for a in self.reader.get("trend_coefficients").split(",")]

    @property
    def percentage_outliers(self):
        """
        Get the percentage of outliers from the configuration.

        Returns:
        - float: The percentage of outliers specified in the configuration.
        """
        return float(self.reader.get("outliers_percentage"))

    @property
    def missings_percentage(self):
        """
        Get the missing data percentage from the configuration.

        Returns:
        - float: The missing data percentage specified in the configuration.
        """
        return float(self.reader.get("missings_percentage"))

    @property
    def data_type(self):
        """
        Get the data type from the configuration.

        Returns:
        - str: The data type specified in the configuration, as a string.
        """
        return DataTypeEnum[self.reader.get("data_type")].value

    @property
    def min_data_value(self):
        """
        Get the min value of the dataset to be generated.

        Returns:
        - float : The minimum value as a float
        """
        return float(self.reader.get("min_value"))

    @property
    def max_data_value(self):
        """
        Get the max value of the dataset to be generated.

        Returns:
        - float : The maximum value as a float
        """
        return float(self.reader.get("max_value"))
