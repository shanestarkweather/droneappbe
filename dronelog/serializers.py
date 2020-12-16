from rest_framework import serializers
from .models import PreFlight, Flight


class PreFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreFlight
        fields = ('id', 'pilot', 'date', 'time', 'location',
                  'drone_reg', 'weather', 'obstructions', 'takeoff_clear')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('preflight_id', 'pilot', 'preflight_date', 'preflight_time', 'preflight_location',
                  'preflight_drone_reg', 'preflight_weather', 'duration', 'incidents')
