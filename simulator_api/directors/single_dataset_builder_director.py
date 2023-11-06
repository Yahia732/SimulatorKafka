import pandas as pd

from configuration_manager.configuration_facade import ConfigurationFacade
from time_series_transformers.missings_transformer import MissingsTransformer
from time_series_transformers.normalizer_transformer import MinMaxScalerTransformer
from time_series_transformers.outlier_transformer import OutlierTransformer

import matplotlib.pyplot as plt


class SingleDatasetDirector:
    def __init__(self, builder, configuration_reader: ConfigurationFacade):
        # the director is responsible for building more than one product
        # implement different directors , one may run  parallel builders
        # another may run sequentially
        # one may run all combinations
        # one may choose random from array
        self.builder = builder
        self.configurator = configuration_reader

    def build(self):
        self.builder.set_trend(self.configurator.trend_coefficients)

        for component in self.configurator.seasonality:
            self.builder.set_seasonality(component["seasonality"], float(component["amplitude"]),
                                         float(component["multiplier"]),
                                         float(component["phase_shift"]))

        self.builder.set_cycles(self.configurator.cyclic_amplitude, self.configurator.cyclic_period)

        normalizer = MinMaxScalerTransformer(self.configurator.min_data_value, self.configurator.max_data_value)

        self.builder.set_normalizer(normalizer)

        self.builder.set_noise(self.configurator.noise_level)

        product = self.builder.product

        # add  outliers

        data_with_outliers = OutlierTransformer(self.configurator.percentage_outliers, self.configurator.min_data_value,
                                                self.configurator.max_data_value).transform(
            product.dataset_values)

        # add missings
        data_with_missings = MissingsTransformer(self.configurator.missings_percentage).transform(data_with_outliers)
        final_dataframe = pd.DataFrame(data_with_missings, index=product.time_series_index)

        # plot data frame
        final_dataframe.plot()
        plt.show()

        return final_dataframe
