from rest_framework import serializers
from .models import Simulator, Dataset, Seasonality


class seasonality_serializer(serializers.ModelSerializer):
    class Meta:
        model = Seasonality
        fields = "__all__"


class dataset_serializer(serializers.ModelSerializer):
    seasonality = seasonality_serializer(many=True, read_only=True)
    class Meta:
        model = Dataset
        fields = "__all__"



class simulator_serializer(serializers.ModelSerializer):
    dataset=dataset_serializer(many=True,read_only=True)
    class Meta:
        model = Simulator
        fields = "__all__"


