from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

# dummy booking
# bookings = [
#     {
#         'booking_id':'1',
#         'name':'Tine Ganda',
#         'from':'HWR Avenue, D15',
#         'to':'Tyrellstown, D15',
#         'date_created':'01/02/2024',
#         'item_type':'Large Box 30x30x30',
#         'description':'Bowling Ball',
#         'price':'10',
#         'status':'Accepted',
#         'driver':'Baby Driver'
#     },
#     {
#         'booking_id':'2',
#         'name':'Jade Pretty',
#         'from':'HWR Avenue, D15',
#         'to':'Bay Meadows, D15',
#         'date_created':'01/02/2024',
#         'item_type':'Large Box 30x30x30',
#         'description':'Basket Ball',
#         'price':'5',
#         'status':'Completed',
#         'driver':'Baby Driver'
#     },
#     {
#         'booking_id':'3',
#         'name':'Jared Pogi',
#         'from':'HWR Avenue, D15',
#         'to':'Huntstown, D15',
#         'date_created':'02/02/2024',
#         'item_type':'Small Box 10x10x10',
#         'description':'Tennis Ball',
#         'price':'3',
#         'status':'Pending',
#         'driver':''
#     },
# ]


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
            return redirect('bookings')
        else:
            return render(request, 'booking/booking_form.html', {'form': form})
    # return HttpResponse('<h1>Create Booking Here</h1>')

