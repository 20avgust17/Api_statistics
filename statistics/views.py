from django.db.models import ExpressionWrapper, F, DecimalField
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from statistics.models import Statistics
from statistics.serializers import SpcCpmStatisticsSerializers, StatisticsSerializers


class CreateStatistic(CreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializers


class StatisticsList(generics.ListAPIView):
    queryset = Statistics.objects.all().annotate(
        spc=ExpressionWrapper(F('cost') * 1.0 / F('clicks'), output_field=DecimalField())).annotate(
        cpm=ExpressionWrapper((F('cost') * 1.0 / F('views')) * 1000, output_field=DecimalField()))
    serializer_class = SpcCpmStatisticsSerializers
    filter_backends = [OrderingFilter]
    ordering_fields = ['cost', 'views', 'date', 'clicks', 'pk']
    ordering = ['date']


class ResetStatistics(generics.RetrieveDestroyAPIView):
    queryset = Statistics.objects.all().annotate(
        spc=ExpressionWrapper(F('cost') * 1.0 / F('clicks'), output_field=DecimalField())).annotate(
        cpm=ExpressionWrapper((F('cost') * 1.0 / F('views')) * 1000, output_field=DecimalField()))
    serializer_class = StatisticsSerializers
