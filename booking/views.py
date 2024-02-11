from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def home(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request,'booking/home.html', context)


def about(request):
    return render(request, 'booking/about.html')


@login_required
def create_booking(request):
    if request.method == 'GET':
        context = {'form': BookingForm()}
        return render(request, 'booking/booking_form.html', context)
    elif request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successfully created.')
            return redirect('bookings')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'booking/booking_form.html', {'form': form})

