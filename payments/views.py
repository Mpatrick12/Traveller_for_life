from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings

from tours.models import Booking
from .models import Payment
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def payments_home(request):
    return render(request, 'payments/home.html')

def process_payment(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        if request.method == 'POST':
        
            stripe.PaymentIntent.create(
                 amount=int(booking.total_price * 100),
                 currency='usd',
                 payment_method_types=['card'],
                 )
            Payment.objects.create(
                booking=Booking,
                amount=booking.total_price,
                payment_status='Completed',
                )
            return redirect('payment_success')
        return render(request, 'payments/checkout.html', {'booking': booking})

def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failed(request):
    return render(request, 'payments/payment_failed.html')

# Create your views here.
