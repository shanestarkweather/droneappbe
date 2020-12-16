from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PreFlightSerializer, FlightSerializer
from .models import PreFlight, Flight


class PreFlightViewSet(viewsets.ModelViewSet):
    queryset = PreFlight.objects.all()
    serializer_class = PreFlightSerializer


# class PreFlightList(generics.ListCreateAPIView):
#     queryset = PreFlight.objects.all()
#     serializer_class = PreFlightSerializer


# class PreFlightDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PreFlight.objects.all()
#     serializer_class = PreFlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# class FlightList(generics.ListCreateAPIView):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer


# class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer
