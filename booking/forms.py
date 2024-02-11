import datetime

from django import forms
from django.forms import ModelForm
from django.utils import timezone

from users.models import CustomUser
from .models import Booking

PAYMENT_TYPES= [
    ('CASH_ON_PICKUP', 'Cash on Pickup'),
    ('CASH_ON_DELIVERY', 'Cash on Delivery'),
    ('CARD', 'Credit/Debit Card')
]

PARCEL_TYPES= [
    ('SMALL_PACKET', 'Small Packet/Envelope'),
    ('MEDIUM_BOX', 'Medium(30x30x30 cm)'),
    ('LARGE_BOX', 'Large(40x40x40 cm)'),
    ('SPECIALTY_BOX', 'Cooler/Thermal Box'),
    ('CUSTOM_SIZE', 'Custom Size Box')
]



class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['pickup','pickup_time', 'sender_name', 'sender_contact_no',
                  'dropoff', 'recipient_name', 'recipient_contact_no', 'parcel_type',
                  'description', 'parcel_type', 'payment_type', 'booked_by', 'courier_fee', 'status']
        labels = {
            'pickup':"Pick-up From",
            'pickup_time':"Pick-up Date/Time",
            'sender_name':"Sender",
            'sender_contact_no':"Contact No.",
            'dropoff':"Drop-off To",
            'recipient_name':"Recipient",
            'recipient_contact_no':"Contact No.",
            'parcel_type':"Parcel Type",
            'description':"Item Description",
            'courier_fee' : "Courier Fee",
            'payment_type':"Payment Type",
            'status': 'Status'
        }
        widgets = {
            'payment_type': forms.Select(choices=PAYMENT_TYPES),
            'parcel_type': forms.Select(choices=PARCEL_TYPES)
        }
