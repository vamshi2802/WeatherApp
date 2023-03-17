# Generated by Django 4.1.7 on 2023-03-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5)),
                ('station_id', models.CharField(max_length=15)),
            ],
            options={
                'unique_together': {('station_id', 'year')},
            },
        ),
    ]
