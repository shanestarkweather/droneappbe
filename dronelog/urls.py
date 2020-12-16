from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreFlightViewSet, FlightViewSet

router = DefaultRouter()
router.register(r'preflights', PreFlightViewSet, basename='preflight')
router.register(r'flights', FlightViewSet, basename='flight')
urlpatterns = router.urls
