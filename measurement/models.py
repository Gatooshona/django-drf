from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, null=True)
