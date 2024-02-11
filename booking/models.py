from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Booking(models.Model):

    pickup = models.CharField(max_length=200)
    pickup_time = models.DateTimeField(default=timezone.now)
    sender_name = models.CharField(max_length=100)
    sender_contact_no = models.CharField(max_length=30)
    dropoff = models.CharField(max_length=200)
    recipient_name = models.CharField(max_length=100)
    recipient_contact_no = models.CharField(max_length=30)
    parcel_type = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    courier_fee = models.DecimalField(max_digits=6,decimal_places=2)
    payment_type = models.CharField(max_length=30)
    booked_date = models.DateField(default=timezone.now)
    booked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='OPEN')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-booked_date']
