from django.shortcuts import get_object_or_404, redirect, render
from .models import Tour
from django.contrib.auth.decorators import login_required
from .models import Tour, Booking
from django.http import HttpResponse



def tour_list(request):
    tours = Tour.objects.all()
    location = request.GET.get('location')
    price = request.GET.get('price')
    if location:
        tours = tours.filter(location__name__icontains=location)
    if price:
        tours = tours.filter(price__lte=price)
    return render(request, 'tours/tour_list.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tours/tour_detail.html', {'tour': tour})

def book_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        Booking.objects.create(user=request.user, tour=tour)
        return redirect('my_bookings')
    return render(request, 'tours/booking.html', {'tour': tour})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'tours/my_bookings.html', {'bookings': bookings})

@login_required
def operator_dashboard(request):
    tours = Tour.objects.filter(tour_operator=request.user)
    bookings = Booking.objects.filter(tour__in=tours)
    return render(request, 'tours/operator_dashboard.html', {'tours': tours, 'bookings': bookings})

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    # Add your search logic here
    return HttpResponse(f"Search results for: {query}")




# Create your views here.
