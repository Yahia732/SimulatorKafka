

class CsvSerializer:
    """
    A serializer for extracting specific fields from a CSV file and returning them as a dictionary.
    """

    def __init__(self, csv_file):
        """
        Initialize a CsvSerializer instance.

        Parameters:
        - csv_file: The CSV file containing data to be serialized.

        """
        self.file = csv_file

    def __dict__(self):
        """
        Serialize the CSV data into a dictionary.

        Returns:
        - dict: A dictionary containing selected fields from the CSV data.

        """
        return {
            "noise_level": self.file["noise_level"],
            "start_date": self.file["start_date"],
            "end_date": self.file["end_date"],
            "frequency": self.file["frequency"],
            "missings_percentage": self.file["missings_percentage"],
            "outliers_percentage": self.file["outliers_percentage"],
            "data_type": self.file["data_type"],
            "trend_coefficients": self.file["trend_coefficients"],
            "seasonality": self.file["seasonality"],
            "cyclic_period": self.file["cyclic_period"],
            "min_value": self.file["min_value"],
            "max_value": self.file["max_value"]

        }
