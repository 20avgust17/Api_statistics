from rest_framework import serializers
from statistics.models import Statistics


class SpcCpmStatisticsSerializers(serializers.ModelSerializer):
    spc = serializers.DecimalField(max_digits=100, decimal_places=2)
    cpm = serializers.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        model = Statistics
        fields = '__all__'


class StatisticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'
