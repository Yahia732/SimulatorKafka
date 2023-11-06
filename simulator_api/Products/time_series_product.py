import pandas as pd

from simulator_api.enums.data_type_enum import DataTypeEnum
import numpy as np


class TimeSeriesProduct:
    def __init__(self, start_date, end_date, freq, type):
        self._start_date = start_date
        self._end_date = end_date
        self._freq = freq
        self._time_series_index = self._set_initial_time_series()
        self._type = type

    def _set_initial_time_series(self):
        return pd.date_range(start=self._start_date, end=self._end_date,
                             freq=self._freq)

    @property
    def time_series_index(self):
        return self._time_series_index

    @property
    def trend(self):
        if hasattr(self, "_trend"):
            return self._trend
        elif self._type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(len(self.time_series_index))

    @trend.setter
    def trend(self, value):
        self._trend = value

    @property
    def seasonality(self):
        if hasattr(self, "_seasonality"):
            return self._seasonality
        elif self._type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(len(self.time_series_index))

    @seasonality.setter
    def seasonality(self, seasonality_series):
        if self._type == DataTypeEnum.ADDITIVE.value:
            self._seasonality = self.seasonality + seasonality_series
        elif self._type == DataTypeEnum.MULTIPLICATIVE.value:
            self._seasonality = self.seasonality * seasonality_series

    @property
    def noise(self):
        if hasattr(self, "_noise"):
            return self._noise
        elif self._type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(self.time_series_index.shape)

    @noise.setter
    def noise(self, value):
        self._noise = value

    @property
    def cycle(self):
        if hasattr(self, "_cycle"):
            return self._cycle
        elif self._type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(self.time_series_index.shape)

    @cycle.setter
    def cycle(self, value):
        self._cycle = value

    @property
    def dataset_values(self):
        if hasattr(self, "_dataset_values"):
            return self._dataset_values
        else:
            raise Exception("Dataset hasn't yet not been calculated !")

    @dataset_values.setter
    def dataset_values(self, value):
        self._dataset_values = value
