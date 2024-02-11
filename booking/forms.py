from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup','pickup_time', 'sender_name', 'sender_contact_no',
                  'dropoff', 'recipient_name', 'recipient_contact_no', 'parcel_type',
                  'description', 'parcel_type', 'payment_type', 'booked_by', 'courier_fee', 'status']
