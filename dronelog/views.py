from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PreFlightSerializer, FlightSerializer
from .models import PreFlight, Flight


class PreFlightViewSet(viewsets.ModelViewSet):
    queryset = PreFlight.objects.all()
    serializer_class = PreFlightSerializer

    def perform_create(self, serializer):
        serializer.save(pilot=self.request.user)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
