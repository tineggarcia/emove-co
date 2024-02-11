from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def edit_booking(request, id):
    try:
        booking = Booking.objects.get(pk=id)
        if request.method == 'GET':
            context = {'form': BookingForm(instance=booking), 'id': id}
            return render(request, 'booking/booking_form.html', context)
    except Booking.DoesNotExist:
        messages.error(request, 'Booking does not exists! Only select from below bookings.')
        return redirect('bookings')


