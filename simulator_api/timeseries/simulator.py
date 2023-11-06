import logging
import os

import pandas as pd
from django.db import close_old_connections
import django

from simulator_api.configuration_manager.configuration_facade import ConfigurationFacade
from simulator_api.configuration_manager.configuration_reader.kafka_reader import KafkaReader
from simulator_api.data_producers.producers_builders.kafka_producer_builder import KafkaProducerBuilder
from simulator_api.directors.mutli_datasets_builders_director import MutliDatasetsDirector
from simulator_api.serializers import simulator_serializer

django.setup()
from simulator_api import models
#from simulator_api.configuration_manager.configuration_facade import ConfigurationFacade
#from simulator_api.configuration_manager.configuration_reader.kafka_reader import KafkaReader
from simulator_api.data_producers.producer_factory import ProducerFactory
from simulator_api.data_producers.producers_builders.csv_producer_builder import CsvProducerBuilder
#from simulator_api.data_producers.producers_builders.kafka_producer_builder import KafkaProducerBuilder

from simulator_api.timeseries.configuration_manager import SimulatorConfigurationManager
import json


class Simulator:
    def __init__(self, simulator_data):
        simulator_data = json.loads(simulator_data)
        simulator = SimulatorConfigurationManager(simulator_data)
        self.start_date = simulator.get_start_date()
        self.end_date = simulator.get_end_date()
        self.data_size = simulator.get_data_size()
        self.series_type = simulator.get_series_type()
        self.datasets = simulator.get_datasets()
        self.producer_type = simulator.get_producer_type()
        self.file_name = simulator.get_name()







def simulate_simulator(simulator_id):

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")



    try:

        close_old_connections()
        # Simulate some background process here
        simulator = models.Simulator.objects.get(id=simulator_id)



        # producer_factory.register_builder("Kafka", KafkaProducerBuilder())
        # producer = producer_factory.create("Kafka", location="localhost:9092")
        # producer.produce(simulator)
        # Kafka_data=ConfigurationFacade(KafkaReader("localhost:9092","Read Kafka",simulator_id))
        d = MutliDatasetsDirector(simulator)
        for i, dataset in enumerate(d.build()):
            producer_factory = ProducerFactory()
            producer_factory.register_builder("Kafka", KafkaProducerBuilder())
            producer = producer_factory.create("Kafka", location="localhost:9092")
            producer.produce(simulator)
            Kafka_data=ConfigurationFacade(KafkaReader("localhost:9092","Read Kafka",simulator_id))
            producer_factory.register_builder("CSV", CsvProducerBuilder())
            producer = producer_factory.create("CSV", location=f"generated_datasets/test_dataset_{i}.csv")
            producer.produce(pd.DataFrame(Kafka_data))

        close_old_connections()
        simulator.status = 'Succeeded'
        simulator.save()

    except Exception as e:
        # Update the simulator status when the task is completed
        print(e)
        simulator = models.Simulator.objects.get(id=simulator_id)
        simulator.status = 'Failed'
        simulator.save()
        logging.error(f'Error in simulation for simulator {simulator_id}: {str(e)}')
