# Generated by Django 4.2.5 on 2023-11-02 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "simulator_api",
            "0018_rename_outlier_presentation_dataset_outlier_percentage",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="attribute_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dataset",
            name="generator_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="simulator",
            name="data_size",
            field=models.IntegerField(
                null=True, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AddField(
            model_name="simulator",
            name="sink_name",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="simulator",
            name="end_date",
            field=models.DateTimeField(null=True),
        ),
    ]