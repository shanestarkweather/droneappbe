from django.db import models
from users.models import User


class PreFlight(models.Model):
    pilot = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='preflights')
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    drone_reg = models.CharField(max_length=100)
    weather = models.TextField(blank=True)
    obstructions = models.TextField(blank=True)
    takeoff_clear = models.BooleanField(blank=False)

    def __str__(self):
        return f'{self.pilot.first_name} {self.pilot.last_name}, {self.location}, {self.date}, {self.time}'


class Flight(models.Model):
    preflight = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    duration = models.CharField(max_length=100)
    incidents = models.TextField(blank=True)

    def __str__(self):
        return f'{self.location}, {self.date}, {self.time}'
