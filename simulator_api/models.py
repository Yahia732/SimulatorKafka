from django.db import models


class Simulator(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    time_series_type = models.CharField(max_length=14,default="")
    producer_type = models.CharField(max_length=10,default="")
    use_case_name = models.CharField(max_length=30,default="")
    meta_data = models.CharField(max_length=400,default="")
    status = models.CharField(max_length=10, default='Submitted')

    process_id = models.IntegerField(null=True,default=0)
    sink_name = models.CharField(max_length=15, default="")


class Dataset(models.Model):
    Frequency = models.CharField(max_length=4,default="")
    Cycle_amplitude = models.FloatField(default=0)
    Cycle_frequency = models.FloatField(default=0)
    Noise_level = models.FloatField(default=0)
    trend_coefficient = models.FloatField(default=0)
    Missing_percentage = models.FloatField(default=0)
    Outlier_percentage = models.FloatField(default=0)


    simulator_id = models.ForeignKey(Simulator, on_delete=models.CASCADE, related_name="Dataset", null=True)
    generator_id = models.IntegerField(null=True)
    attribute_id = models.IntegerField(null=True)


class Seasonality(models.Model):
    phase_shift = models.FloatField(default=0)
    frequency_type = models.CharField(max_length=10)
    frequency_multiplier = models.FloatField(default=0)
    dataset_id = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="Seasonality",
                                   null=True)
