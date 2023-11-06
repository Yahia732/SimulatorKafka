class kafkaSerializer:
    """
    A serializer for extracting specific fields from a kafka and returning them as a dictionary.
    """

    def __init__(self, kafka_file):
        """
        Initialize a kafkaSerializer instance.

        Parameters:
        - kafka_file: The kafka file containing data to be serialized.

        """
        self.file = kafka_file

    def __dict__(self):
        """
        Serialize the kafka data into a dictionary.

        Returns:
        - dict: A dictionary containing selected fields from the kakfa data.

        """
        return {
            "attributeId": self.file["attributeId"],
            "value": self.file["'value"],
            "timestamp": self.file["timestamp"],
            "assetId": self.file["assetId"]


        }