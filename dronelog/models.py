from django.db import models
from django.contrib.auth.models import AbstractUser


class PreFlight(models.Model):
    pilot = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    drone_reg = models.CharField(max_length=100)
    weather = models.TextField(blank=True)
    obstructions = models.TextField(blank=True)
    takeoff_clear = models.BooleanField(blank=False)

    def __str__(self):
        return self.pilot - self.location - self.date - self.time


class Flight(models.Model):
    pilot = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    date = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    time = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    location = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    drone_reg = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    weather = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    duration = models.CharField(max_length=100)
    incidents = models.TextField(blank=True)

    def __str__(self):
        return self.location - self.date - self.time
