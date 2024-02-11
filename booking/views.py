from django.shortcuts import render
from django.http import HttpResponse

# dummy booking
bookings = [
    {
        'booking_id':'1',
        'name':'Tine Ganda',
        'from':'HWR Avenue, D15',
        'to':'Tyrellstown, D15',
        'date_created':'01/02/2024',
        'item_type':'Large Box 30x30x30',
        'description':'Bowling Ball',
        'price':'10',
        'status':'Accepted',
        'driver':'Baby Driver'
    },
    {
        'booking_id':'2',
        'name':'Jade Pretty',
        'from':'HWR Avenue, D15',
        'to':'Bay Meadows, D15',
        'date_created':'01/02/2024',
        'item_type':'Large Box 30x30x30',
        'description':'Basket Ball',
        'price':'5',
        'status':'Completed',
        'driver':'Baby Driver'
    },
    {
        'booking_id':'3',
        'name':'Jared Pogi',
        'from':'HWR Avenue, D15',
        'to':'Huntstown, D15',
        'date_created':'02/02/2024',
        'item_type':'Small Box 10x10x10',
        'description':'Tennis Ball',
        'price':'3',
        'status':'Pending',
        'driver':''
    },
]


def home(request):
    context = {
        'bookings': bookings
    }
    return render(request,'booking/home.html', context)
    # return HttpResponse('<h1>Booking Home</h1>')


def about(request):
    return render(request, 'booking/about.html')
    # return HttpResponse('<h1>About Us</h1>')
