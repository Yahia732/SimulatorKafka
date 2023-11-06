from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse  # Import JsonResponse from django.http
from .models import Simulator
from django.views import View
from multiprocessing import Process
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import psutil
from rest_framework import viewsets, status
from rest_framework.response import Response
from .timeseries.simulator import simulate_simulator
from .serializers import *



class Add_Simulator(ListCreateAPIView):
    queryset = Simulator.objects.all()
    serializer_class = simulator_serializer

    def create(self, request, *args, **kwargs):
        data = request.data
        simulator_serializer_instance = simulator_serializer(data=data)




        if simulator_serializer_instance.is_valid():
            datasets = data.pop('Dataset')

            simulator = simulator_serializer_instance.save()
            simulator_id = simulator.id
            for dataset in datasets:
                dataset_serializer_instance = dataset_serializer(data=dataset)
                dataset['simulator_id'] = simulator_id
                if dataset_serializer_instance.is_valid():
                    seasonality = dataset.pop('Seasonality')
                    simulator_dataset = dataset_serializer_instance.save()
                    dataset_id = simulator_dataset.id
                    for season in seasonality:
                        seasonality_serializer_instance = seasonality_serializer(data=season)
                        season['dataset_id'] = dataset_id
                        if seasonality_serializer_instance.is_valid():
                            seasonality_serializer_instance.save()

            return Response("Time series added", status=status.HTTP_200_OK)



@method_decorator(csrf_exempt, name='dispatch')
class RunSimulatorView(View):

    def post(self, request, simulator_id):

        try:
            simulator = Simulator.objects.get(id=simulator_id)

            if simulator.status == 'Running':
                return JsonResponse({"message": "Simulator is already running"}, status=200)  # Return a JsonResponse
            process = Process(target=simulate_simulator, args=(simulator_id,))
            process.start()

            simulator.process_id = process.pid
            simulator.status = 'Running'
            simulator.save()

            return JsonResponse({"message": "Simulator is running"}, status=200)  # Return a JsonResponse

        except Exception as e:
            return JsonResponse({"message": "Error: " + str(e)}, status=502)  # Return a 502 response for other exceptions



@method_decorator(csrf_exempt, name='dispatch')
class StopSimulatorView(View):

    def post(self, request, simulator_id):

        try:
            # Find and terminate the simulator process by simulator_id
            simulator = Simulator.objects.get(id=simulator_id)
            if simulator.status == 'Running':

                simulator.status = 'Stopped'
                simulator.save()
                return Response("Simulator is stopped", status=200)
            else:
                return Response("Simulator is not running", status=200)
        except Exception :
            return Response("Error", status=502)
