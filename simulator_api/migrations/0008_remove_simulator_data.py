# Generated by Django 4.2.5 on 2023-09-07 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulator_api', '0007_rename_datasets_simulator_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulator',
            name='data',
        ),
    ]