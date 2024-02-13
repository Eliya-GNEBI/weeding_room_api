from django.shortcuts import render
from rest_framework import generics

from weddingroom.serializers import SalleSerializer
from .models import Reservation, Salle
from rest_framework import serializers
# Create your views here.
from rest_framework import generics
from .serializers import ReservationSerializer

from .models import Reservation


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
class SalleListCreateView(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

class SalleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
