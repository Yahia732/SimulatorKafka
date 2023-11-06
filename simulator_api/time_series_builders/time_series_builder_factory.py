from simulator_api.enums.data_type_enum import DataTypeEnum
from simulator_api.time_series_builders.builders.additive_builder import AdditiveBuilderInterface
from simulator_api.time_series_builders.builders.builder_interface import BuilderInterface


class TimeSeriesBuilderFactory:
    """
    A factory class for creating time series builders based on data types.

    This class provides a method to create time series builders based on the
    specified data type, allowing for the dynamic creation of builders
    for different types of time series data.

    Methods:
    - create(cls, data_type: str, **kwargs): Create a time series builder based
      on the specified data type.

    Attributes:
    - _factory_supported_classes (dict): A dictionary that maps data type names
      to their corresponding builder classes.
    """

    @classmethod
    def create(cls, data_type: str, **kwargs) -> BuilderInterface:
        """
        Create a time series builder based on the specified data type.

        Parameters:
        - data_type (str): The data type for which to create a time series builder.
        - **kwargs: Additional keyword arguments to pass to the builder constructor.

        Returns:
        - Builder: An instance of the time series builder corresponding to the
          specified data type.

        Raises:
        - Exception: If the specified data type is not supported by the factory.


        """
        _factory_supported_classes = {DataTypeEnum.ADDITIVE.value: AdditiveBuilderInterface}
        if data_type in _factory_supported_classes:
            subclass = _factory_supported_classes.get(data_type)
            return subclass(**kwargs)
        else:
            raise Exception(f'Cannot find "{data_type}"')
