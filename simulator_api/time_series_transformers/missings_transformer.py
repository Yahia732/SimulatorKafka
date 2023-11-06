from simulator_api.time_series_transformers.transformer import Transformer
import numpy as np


class MissingsTransformer(Transformer):
    def __init__(self, missings_percentage: float):
        self.missings_percentage = missings_percentage

    def transform(self, time_series):
        num_missing = int(len(time_series) * self.missings_percentage)
        missing_indices = np.random.choice(len(time_series), size=num_missing, replace=False)

        data_with_missing = time_series.copy()
        data_with_missing[missing_indices] = np.nan

        return data_with_missing
