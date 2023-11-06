
from django.urls import path
from .views import *

urlpatterns = [
    path('', Add_Simulator.as_view()),

    path('api/run_simulator/<int:simulator_id>', RunSimulatorView.as_view(), name='run-simulator'),
    path('api/stop_simulator/<int:simulator_id>', StopSimulatorView.as_view(), name='stop-simulator')]
