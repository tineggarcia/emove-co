from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookings'),
    path('about/', views.about, name='about'),
    path('booking/create/', views.create_booking, name='booking-create'),
    path('booking/edit/<int:id>/', views.edit_booking, name='booking-edit'),
    path('booking/delete/<int:id>/', views.delete_booking, name='booking-delete'),
]