from simulator_api.time_series_components.component import Component
import numpy as np


class NoiseComponent(Component):
    def __init__(self, time_series_data: np.ndarray, signal_to_noise_ratio:float):
        self.time_series_data = time_series_data
        self.signal_to_noise_ratio = signal_to_noise_ratio

    def calculate(self):
        # Step 1: Calculate the variance of the data
        signal_power = np.var(self.time_series_data)

        # Step 2: Determine the Desired SNR (in dB)
        desired_snr_db = self.signal_to_noise_ratio  # Desired SNR in dB

        # Step 3: Calculate the Noise Power (in dB and linear scale)
        noise_power_db = signal_power - desired_snr_db

        noise_power = 10 ** (noise_power_db / 10)

        # Step 4: Generate Noise with the Calculated Power
        noise_stddev = np.sqrt(noise_power)
        noise = np.random.normal(0, noise_stddev, len(self.time_series_data))

        return noise
