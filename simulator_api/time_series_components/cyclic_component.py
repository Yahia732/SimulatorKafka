from pandas import DatetimeIndex

from simulator_api.time_series_components.component import Component
import numpy as np
import random


class CyclicComponent(Component):
    def __init__(self, time_series: DatetimeIndex, amplitude: float, cycle_period: float):
        self.time_series_index = time_series
        self.amplitude = amplitude
        self.cycle_period = cycle_period

    def calculate(self):
        return self.amplitude * np.sin(2 * np.pi * self.time_series_index.year / self.cycle_period)
