import pandas as pd
from simulator_api.time_series_builders.time_series_builder_factory import TimeSeriesBuilderFactory
from simulator_api.time_series_transformers.missings_transformer import MissingsTransformer
from simulator_api.time_series_transformers.normalizer_transformer import MinMaxScalerTransformer
from simulator_api.time_series_transformers.outlier_transformer import OutlierTransformer


class MutliDatasetsDirector:
    def __init__(self, configuration_readers: list):
        # the director is responsible for building more than one product (one dataset)
        self.configurators = configuration_readers

    def build(self):
        for configurator in self.configurators:
            builder = TimeSeriesBuilderFactory.create(configurator.data_type,
                                                      start_date=configurator.start_date, end_date=configurator.end_date,
                                                      freq=configurator.frequency)
            builder.set_trend(configurator.trend_coefficients)

            for component in configurator.seasonality:
                builder.set_seasonality(component["seasonality"], float(component["amplitude"]),
                                        float(component["multiplier"]),
                                        float(component["phase_shift"]))

            builder.set_cycles(configurator.cyclic_amplitude, configurator.cyclic_period)

            normalizer = MinMaxScalerTransformer(configurator.min_data_value, configurator.max_data_value)

            builder.set_normalizer(normalizer)

            builder.set_noise(configurator.noise_level)

            product = builder.product

            # add  outliers

            data_with_outliers = OutlierTransformer(configurator.percentage_outliers, configurator.min_data_value,
                                                    configurator.max_data_value).transform(
                product.dataset_values)

            # add missings
            data_with_missings = MissingsTransformer(configurator.missings_percentage).transform(
                data_with_outliers)
            final_dataframe = pd.DataFrame(data_with_missings, index=product.time_series_index)

            yield final_dataframe
