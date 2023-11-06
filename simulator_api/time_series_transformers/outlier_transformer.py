from simulator_api.time_series_transformers.transformer import Transformer
import numpy as np


class OutlierTransformer(Transformer):
    def __init__(self, outlier_percentage: float, min_value: float, max_value: float):
        self.outlier_percentage = outlier_percentage
        self._anomaly_mask = None
        self.min_value = min_value
        self.max_value = max_value

        # TODO: make the distribution type a paramter instad of hard coded

    def get_anomaly_mask(self):
        return self._anomaly_mask

    def transform(self, time_series: np.ndarray):
        print("UUUUUUUUUUUUUU")
        print(type(time_series))
        num_outliers = int(len(time_series) * self.outlier_percentage)
        outlier_indices = np.random.choice(len(time_series), num_outliers, replace=False)
        # data_with_outliers = pd.Series(data.copy())
        data_with_outliers = time_series.copy()
        outliers = np.random.uniform(self.min_value, self.max_value, num_outliers)
        if len(outliers) > 0:
            self._anomaly_mask = np.zeros(len(data_with_outliers), dtype=bool)
            data_with_outliers[outlier_indices] = outliers
            self._anomaly_mask[outlier_indices] = True
        return data_with_outliers
