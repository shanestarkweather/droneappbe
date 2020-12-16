from rest_framework import serializers
from .models import PreFlight, Flight


class PreFlightSerializer(serializers.ModelSerializer):
    pilot = serializers.ReadOnlyField(
        source='pilot.id',
        read_only=True
    )

    class Meta:
        model = PreFlight
        fields = ('id', 'pilot', 'date', 'time', 'location',
                  'drone_reg', 'weather', 'obstructions', 'takeoff_clear')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('preflight', 'id', 'duration', 'incidents')
