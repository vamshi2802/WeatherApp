from django.db import models


class WeatherData(models.Model):
    date = models.CharField(max_length=8)
    max_temp = models.FloatField
    min_temp = models.FloatField
    precipitation = models.FloatField
    station_id = models.CharField(max_length=15)

    class Meta:
        unique_together = (('station_id', 'date'),)
        db_table = 'weather_data'


class WeatherStats(models.Model):
    year = models.CharField(max_length=5)
    avg_max_temp = models.FloatField
    avg_min_temp = models.FloatField
    total_acc_precipitation = models.FloatField
    station_id = models.CharField(max_length=15)

    class Meta:
        unique_together = (('station_id', 'year'),)
        db_table = 'weather_stats'
