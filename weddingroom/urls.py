
from django.urls import path
from .views import ReservationListCreateView, ReservationRetrieveUpdateDestroyView, SalleListCreateView, SalleRetrieveUpdateDestroyView

urlpatterns = [
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-retrieve-update-destroy'),
    path('salles/', SalleListCreateView.as_view(), name='salle-list-create'),
    path('salles/<int:pk>/', SalleRetrieveUpdateDestroyView.as_view(), name='salle-retrieve-update-destroy'),
]
