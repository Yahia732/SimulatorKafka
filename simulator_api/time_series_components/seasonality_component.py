from pandas import DatetimeIndex

from simulator_api.time_series_components.component import Component
import numpy as np


class SeasonalityComponent(Component):
    def __init__(self, time_series_index: DatetimeIndex, seasonality_unit: str, seasonality_multiplier: float,
                 amplitude: float, phase_shift: float = 0):
        self.time_series_index = time_series_index
        self.seasonality_unit = seasonality_unit
        self.amplitude = amplitude
        self.phase_shift = phase_shift
        self._seasonality = {
            "Daily": self.amplitude * np.sin(
                2 * np.pi * ((self.time_series_index.hour + 1) / (24 * seasonality_multiplier)) + self.phase_shift),
            "Weekly": self.amplitude * np.sin(
                2 * np.pi * (self.time_series_index.day / (7 * seasonality_multiplier)) + self.phase_shift),
            "Monthly": self.amplitude * np.sin(
                2 * np.pi * (self.time_series_index.dayofyear / (30 * seasonality_multiplier)) + self.phase_shift),
        }

    def calculate(self):
        return self._seasonality.get(self.seasonality_unit)
