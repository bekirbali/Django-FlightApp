from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Passenger, PassengerSerializer,
    Flight, FlightSerializer,
    Reservation, ReservationSerializer
)

# Create your views here.

class FixView(ModelViewSet):
    pass


class PassengerView(FixView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


from rest_framework.permissions import IsAuthenticatedOrReadOnly
class FlightView(FixView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer