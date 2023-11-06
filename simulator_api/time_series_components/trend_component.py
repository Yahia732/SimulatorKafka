from simulator_api.time_series_components.component import Component
import numpy as np
from pandas import DatetimeIndex


class TrendComponent(Component):

    def __init__(self, time_series_index: DatetimeIndex, coefficients: list):
        self.time_series_index = time_series_index
        self.coefficients = coefficients

    def calculate(self):
        trend = 0
        for i, coefficient in enumerate(self.coefficients):
            time_intervals = np.arange(len(self.time_series_index))
            trend += coefficient * time_intervals ** i

        return trend
