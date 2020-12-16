from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreFlightViewSet, FlightViewSet

router = DefaultRouter()
router.register(r'preflights', PreFlightViewSet, basename='preflight')
router.register(r'flights', FlightViewSet, basename='flight')
urlpatterns = router.urls


# urlpatterns = [
#     path('preflight/', views.PreFlightList.as_view(), name='preflight_list'),
#     path('preflight/<int:pk>', views.PreFlightDetail.as_view(),
#          name='preflight_detail'),
#     path('flights/', views.FlightList.as_view(), name='flight_list'),
#     path('flights/<int:pk>', views.FlightDetail.as_view(), name='flight_detail')
# ]
