from simulator_api.enums.data_type_enum import DataTypeEnum
from simulator_api.time_series_builders.builders.builder_interface import BuilderInterface
from simulator_api.time_series_components.cyclic_component import CyclicComponent
from simulator_api.time_series_components.noise_component import NoiseComponent
from simulator_api.time_series_components.seasonality_component import SeasonalityComponent
from simulator_api.Products.time_series_product import TimeSeriesProduct
from simulator_api.time_series_components.trend_component import TrendComponent
from simulator_api.time_series_transformers.transformer import Transformer


class AdditiveBuilderInterface(BuilderInterface):
    def __init__(self, start_date: str, end_date: str, freq: float):
        self.start_date = start_date
        self.end_date = end_date
        self.freq = freq
        self._end_product = TimeSeriesProduct(self.start_date, self.end_date, self.freq, DataTypeEnum.ADDITIVE.value)

    def set_trend(self, coefficients: list):
        trend = TrendComponent(self._end_product.time_series_index, coefficients).calculate()
        self._end_product.trend = trend

    def set_seasonality(self, seasonality: str, amplitude: float, multiplier: float, phase_shift: float):
        seasonality = SeasonalityComponent(self._end_product.time_series_index, seasonality, multiplier, amplitude,
                                           phase_shift).calculate()
        self._end_product.seasonality = seasonality

    def set_normalizer(self, normalizer: Transformer):
        self._normalizer = normalizer

    def set_noise(self, signal_to_noise_ration: float):
        noise = NoiseComponent(self.product.dataset_values, signal_to_noise_ration).calculate()
        self._end_product.noise = noise

    def set_cycles(self, amplitude: float, cycle_period: float):
        cycle = CyclicComponent(self._end_product.time_series_index, amplitude, cycle_period).calculate()
        self._end_product.cycle = cycle

    def _generate_dataset(self):
        output = self._end_product.trend + self._end_product.seasonality + self._end_product.cycle
        if hasattr(self, "_normalizer"):
            output = self._normalizer.transform(output)
        # ADD NOISE after normalisation
        output += self._end_product.noise
        return output

    @property
    def product(self):
        self._end_product.dataset_values = self._generate_dataset()
        return self._end_product
