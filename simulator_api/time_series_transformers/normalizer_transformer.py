from simulator_api.time_series_transformers.transformer import Transformer
from sklearn.preprocessing import MinMaxScaler


class MinMaxScalerTransformer(Transformer):
    def __init__(self, min_value, max_value):
        self.scaler = MinMaxScaler(feature_range=(min_value, max_value))

    def transform(self, time_series):
        return self.scaler.fit_transform(time_series.values.reshape(-1, 1)).reshape(time_series.shape)
