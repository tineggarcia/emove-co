from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

@login_required
def home(request):
    bookings = Booking.objects.filter(booked_by=request.user)
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
        queryset = Booking.objects.filter(booked_by=request.user)
        booking = get_object_or_404(queryset, pk=id)
        if request.method == 'GET':
            context = {'form': BookingForm(instance=booking), 'id': id}
            return render(request, 'booking/booking_form.html', context)
    except Booking.DoesNotExist:
        messages.error(request, 'Booking does not exists! Only select from below bookings.')
        return redirect('bookings')

@login_required
def delete_booking(request, id):
    try:
        queryset = Booking.objects.filter(booked_by=request.user)
        booking = get_object_or_404(queryset, pk=id)
        # booking = Booking.objects.get(pk=id)
        context = {'booking':booking}

        if request.method == 'GET':
            return render(request, 'booking/booking_confirm_delete.html', context)
        elif request.method == 'POST':
            booking.delete()
            messages.success(request,  'The booking has been deleted successfully.')
        return redirect('bookings')

    except Booking.DoesNotExist:
        messages.error(request, 'Booking does not exists! Only select from below bookings.')
        return redirect('bookings')


