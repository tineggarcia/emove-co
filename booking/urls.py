from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookings'),
    path('about/', views.about, name='about'),
    path('booking/create/', views.create_booking, name='booking-create'),
]