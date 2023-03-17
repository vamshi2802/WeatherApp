from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import WeatherData, WeatherStats
from .serializer import WeatherDataSerializer, WeatherStatsSerializer


class Weather(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["date", "station_id"]


class Stats(generics.ListAPIView):
    queryset = WeatherStats.objects.all()
    serializer_class = WeatherStatsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["year", "station_id"]
